"""Import enabled GamePP process names as unreviewed GameDB candidates."""

import hashlib
import json
import re
import sqlite3
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "candidates" / "gamepp-type1.json"
INVALID_NAME = re.compile(r'[<>:"/\\|?*\x00-\x1f]')
EXCLUSIONS = [
    ("launcher", re.compile(r"launcher", re.I)),
    ("editor", re.compile(r"editor", re.I)),
    ("benchmark", re.compile(r"benchmark", re.I)),
    ("installer", re.compile(r"installer|setup|install(?:ing)?(?:\.exe$|[._\s-])|uninstall|unins", re.I)),
    ("helper", re.compile(r"webhelper|helper(?=[._\s-]|$)|daemon|subprocess", re.I)),
    ("updater", re.compile(r"updater|patcher|updateclient|modsupdateui|autopatch|filepatch|eonpatch|_update\.exe$", re.I)),
    ("crash reporter", re.compile(r"crash(?:reporter|handler|pad)|bugreport|errorreport", re.I)),
    ("anti-cheat bootstrap", re.compile(r"anti.?cheat|battleye|beclient|beservice|_(?:be|zk)\.exe$", re.I)),
    ("server", re.compile(r"(?:^|[._\s-])server(?=[._\s-]|$)|dedicatedserver\.exe$|servermanager", re.I)),
    ("configuration tool", re.compile(r"(?:config|configuration|support|flash)?tools?\.exe$|config\.exe$|(?:^|[._\s-])config(?:uration)?\.exe$|textools", re.I)),
    ("mod manager", re.compile(r"modmanager|modorganizer", re.I)),
    ("platform client", re.compile(r"^battle\.net(?:[ .(-]|$)|^application-steam-|steamloader", re.I)),
    ("trainer utility", re.compile(r"v\d[^\\/]*plus\s+\d+\s+trainer", re.I)),
    ("patch utility", re.compile(r"(?:^|[._\s-])patch(?:[._\s-]|\d)|patch\.exe$|swdpatch|riftpatch|selfpatch", re.I)),
]
EXACT_EXCLUSIONS = {
    "hammer.exe": "editor",
    "riotclientservices.exe": "platform service",
    "rockstarservice.exe": "platform service",
    "originwebhelperservice.exe": "platform service",
    "nmservice.exe": "service",
    "seappservice.exe": "service",
    "hngservice.exe": "service",
    "desktopoverlayhost.exe": "overlay",
    "nvstreamer.exe": "streaming service",
    "python.exe": "development runtime",
    "tmodloader.exe": "mod loader",
    "steamvr_room_setup.exe": "configuration tool",
    "aiseesoft screen recorder.exe": "screen recorder",
    "online ios recorder.exe": "screen recorder",
    "velocap hd recorder.exe": "screen recorder",
    "virtualmotioncapture.exe": "capture utility",
    "coherentui_host.exe": "browser helper",
    "godot.windows.opt.tools.64.exe": "game editor",
    "gputool_ctp1.exe": "configuration tool",
    "tmodloaderserver.exe": "server",
    "7daystodieserver.exe": "server",
    "arma2server.exe": "server",
    "eu4_server.exe": "server",
    "huxleymmoserver.exe": "server",
    "iw5mp_server.exe": "server",
    "mohpa_server.exe": "server",
    "rust_server.exe": "server",
    "scumserver.exe": "server",
    "theforestdedicatedserver.exe": "server",
    "empyriondedicated.exe": "server",
    "gtldedicated.exe": "server",
    "four elements trainer.exe": "trainer utility",
    "cheat resource all100000.exe": "cheat utility",
    "haze's multi hack - win 10.exe": "cheat utility",
    "thornsin_cheat.exe": "cheat utility",
    "aibehaviortoolkit-win64-shipping.exe": "development tool",
    "mhclient-gmtool-debug.exe": "development tool",
    "ovr toolkit settings.exe": "VR utility",
    "ovr toolkit.exe": "VR utility",
    "streamingtool-6.2.1-x64.exe": "streaming utility",
    "content manager_5bf5552e_24de00e9.exe": "content manager",
    "csgodemosmanager.exe": "demo manager",
    "hd-multiinstancemanager.exe": "instance manager",
    "sam3_content_manager.exe": "content manager",
    "wbfsmanager.exe": "file manager",
    "mixcastservice.exe": "VR service",
    "visualhost.exe": "host utility",
    "hydraoverlay.exe": "overlay",
    "mhw overlay-142-3-5.exe": "overlay",
    "overlay_win2k.exe": "overlay",
    "mixcastcapture.exe": "capture utility",
    "multicamcapture.exe": "capture utility",
    "remotrserver.exe": "server",
    "vrserver.exe": "server",
    "client_loader.exe": "loader",
    "terrariamodloader.exe": "mod loader",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reason_for(name):
    if not name.casefold().endswith(".exe"):
        return "not an EXE filename"
    if len(name) > 160 or INVALID_NAME.search(name):
        return "invalid EXE filename"
    exact = EXACT_EXCLUSIONS.get(name.casefold())
    if exact:
        return exact
    for reason, pattern in EXCLUSIONS:
        if pattern.search(name):
            return reason
    return None


def main(source):
    source = Path(source).resolve(strict=True)
    before = digest(source)
    with sqlite3.connect(source.as_uri() + "?mode=ro", uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        if db.execute("PRAGMA quick_check").fetchone()[0] != "ok":
            raise ValueError("GamePP database failed integrity check")
        rows = db.execute(
            "SELECT process FROM WhiteBlack WHERE type='1' AND on_off=1"
        ).fetchall()
    if before != digest(source):
        raise ValueError("GamePP database changed during import")

    candidates = {}
    excluded = {}
    for (raw_name,) in rows:
        name = raw_name.strip() if isinstance(raw_name, str) else ""
        reason = reason_for(name)
        key = name.casefold()
        if reason:
            excluded.setdefault(key, {"name": name, "reason": reason})
        else:
            candidates.setdefault(key, name)

    output = {
        "schemaVersion": 1,
        "kind": "unreviewed-process-name-candidates",
        "source": {
            "product": "GamePP",
            "database": source.name,
            "appVersion": source.parents[2].name,
            "sha256": before,
            "table": "WhiteBlack",
            "selection": {"type": "1", "on_off": 1},
        },
        "counts": {
            "selectedRows": len(rows),
            "candidateNames": len(candidates),
            "excludedNames": len(excluded),
        },
        "candidates": sorted(candidates.values(), key=str.casefold),
        "excluded": sorted(excluded.values(), key=lambda item: item["name"].casefold()),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Imported {len(candidates)} candidates; excluded {len(excluded)} names.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python tools/import-gamepp.py PATH_TO_GamePP0.dat")
    main(sys.argv[1])
