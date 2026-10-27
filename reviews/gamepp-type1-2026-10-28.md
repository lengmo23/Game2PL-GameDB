# GamePP 候选补充审核（2026-10-28）

## 范围与结果

沿用 2026-10-26 的 [候选库](../candidates/gamepp-type1.json) 与证据标准，本次针对其中有明确游戏名或可找到官方主 EXE 文档的名称继续审核。GamePP 的 EXE 名称只用于定位候选；每条新增记录同时核对 Steam AppID 和发行商/开发商的主程序资料。

新增 **16 条 verified 游戏记录、17 个主 EXE 名称**。《博德之门 3》的 Vulkan 与 DirectX 11 入口各算一个 EXE 名称。正式库共 35 条记录，其中 34 条 verified、1 条 rejected；23,116 个 GamePP 候选名中，34 个与 verified 主 EXE 名称大小写无关地吻合，另外 **23,082 个未命中**，全部继续留在候选文件。名称命中不代表来源行本身证明了游戏身份。

| Steam AppID / 游戏 | 进入 verified 的 GamePP 候选名 | 官方主程序证据 |
| --- | --- | --- |
| [1086940](https://store.steampowered.com/app/1086940/Baldurs_Gate_3/) Baldur's Gate 3 | `bg3.exe`、`bg3_dx11.exe` | [Larian](https://larian.com/support/faqs/crashing-upon-startup-pc_59) 指明两种渲染入口及 `bin` 目录，另有独立启动器。 |
| [1716740](https://store.steampowered.com/app/1716740/Starfield/) Starfield | `Starfield.exe` | [Bethesda](https://help.bethesda.net/app/answers/detail/a_id/62109/) 指明 Steam 安装目录中的游戏 EXE。 |
| [582010](https://store.steampowered.com/app/582010/Monster_Hunter_World/) Monster Hunter: World | `MonsterHunterWorld.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/5729909044252-Monster-Hunter-World-General-Troubleshooting-Guide-Steam) 指明主程序。 |
| [1446780](https://store.steampowered.com/app/1446780/MONSTER_HUNTER_RISE/) Monster Hunter Rise | `MonsterHunterRise.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/5609349086876-Monster-Hunter-Rise-General-Troubleshooting-Guide-Steam) 指明主程序。 |
| [1364780](https://store.steampowered.com/app/1364780/Street_Fighter_6/) Street Fighter 6 | `StreetFighter6.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/9028228511260-Street-Fighter-6-General-Troubleshooting-Guide-Steam) 指明主程序。 |
| [2050650](https://store.steampowered.com/app/2050650/Resident_Evil_4/) Resident Evil 4 (2023) | `re4.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/8192772494108-Resident-Evil-4-2023-General-Troubleshooting-Guide-Steam) 指明 2023 版主程序；须以 AppID 区分同名 EXE 的 2005 版。 |
| [489830](https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/) Skyrim Special Edition | `SkyrimSE.exe` | [Bethesda](https://help.bethesda.net/app/answers/detail/a_id/45370/) 分别列出游戏 EXE 和 `SkyrimSELauncher.exe`。 |
| [377160](https://store.steampowered.com/app/377160/Fallout_4/) Fallout 4 | `Fallout4.exe` | [Bethesda](https://help.bethesda.net/app/answers/detail/a_id/40902/) 分别列出游戏 EXE 和 `Fallout4Launcher.exe`。 |
| [952060](https://store.steampowered.com/app/952060/Resident_Evil_3/) Resident Evil 3 (2020) | `re3.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/5787244644636-Resident-Evil-3-General-Troubleshooting-Guide-Steam) 区分 `re3.exe` 与《Resident Evil Resistance》的 EXE。 |
| [1196590](https://store.steampowered.com/app/1196590/Resident_Evil_Village/) Resident Evil Village | `re8.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/5598567332508-Resident-Evil-Village-General-Troubleshooting-Guide-Steam) 指明主程序。 |
| [418370](https://store.steampowered.com/app/418370/Resident_Evil_7_Biohazard/) Resident Evil 7 Biohazard | `re7.exe` | [Capcom](https://www.capcom-support.com/hc/en-us/articles/5827833043612-Resident-Evil-7-biohazard-General-Troubleshooting-Guide-Steam) 指明主程序。 |
| [782330](https://store.steampowered.com/app/782330/DOOM_Eternal/) DOOM Eternal | `DOOMEternalx64vk.exe` | [Bethesda](https://help.bethesda.net/app/answers/detail/a_id/50139/) 分别列出游戏 EXE 和 `idTechLauncher.exe`。 |
| [379720](https://store.steampowered.com/app/379720/DOOM/) DOOM (2016) | `DOOMx64.exe` | [Bethesda](https://help.bethesda.net/app/answers/detail/a_id/33908/) 指明 Steam 安装目录中的主程序。 |
| [1151340](https://store.steampowered.com/app/1151340/Fallout_76/) Fallout 76 | `Fallout76.exe` | [Bethesda](https://help.bethesda.net/app/answers/detail/a_id/50679/) 区分游戏 EXE 与 Steam 客户端。 |
| [230410](https://store.steampowered.com/app/230410/Warframe/) Warframe | `Warframe.x64.exe` | [Digital Extremes](https://support.warframe.com/hc/en-us/articles/360044025712-Update-failed) 分别列出游戏 EXE 和 `Launcher.exe`。 |
| [427520](https://store.steampowered.com/app/427520/Factorio/) Factorio | `Factorio.exe` | [Wube FAQ](https://factorio.com/support/faq) 指明 Windows 游戏 EXE；[官方 Wiki](https://wiki.factorio.com/Command_line_parameters) 给出 `bin/x64` 路径。 |

本次没有依据名称推断 Elden Ring、Hogwarts Legacy、Palworld、Helldivers 2 等其它候选的主程序，也没有把启动器、反作弊引导器或服务器程序写入新记录。GameDB 仍需要本机平台身份及安装路径等证据才能参与客户端识别；本次没有修改 Process Lasso 配置。
