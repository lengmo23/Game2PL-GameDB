# Game2PL GameDB

这个目录是社区游戏身份库的仓库原型。`records` 是可审查的数据源，`generated/gamedb-v1.json` 是客户端读取的生成物。

数据库事实记录采用 CC0-1.0，构建与校验脚本采用 MIT；详情见 `LICENSE-DATA` 和 `LICENSE-CODE`。

- `verified`：只有平台 ID 与本机安装证据同时匹配时才能参与识别。
- `pending`：不能进入发布索引，也不能触发 Process Lasso 写入。
- `rejected`：明确的非游戏，用于阻止误判。
- `deprecated`：被替换或合并的旧记录。

`verified` 记录只收录有可复核证据的 Windows 主游戏进程。没有公开稳定平台 ID 的独立客户端使用小写连字符 slug 作为 `platformId`；该 slug 仅用于数据库身份，不会仅凭 EXE 文件名判定本机程序为游戏。启动器、更新器、助手与反作弊服务不进入 `executables`。

运行 `npm run build` 生成索引。发布前应按 `REVIEWING.md` 审核证据；不能仅凭候选 EXE 名称将记录升级为 `verified`。

## GamePP 进程名候选

`candidates/gamepp-type1.json` 保存从本机 GamePP 数据库导入、经过明显非游戏进程过滤的候选 EXE 名称，并附有来源哈希和逐项剔除原因。它只表示 GamePP 将该进程标为启用的 `type=1`；同名文件可能属于不同软件，候选不能单独证明游戏身份或本机安装。

这份候选不属于 `records` 中经证据审核的游戏身份记录，`npm run build` 不会把它写入客户端使用的 `generated/gamedb-v1.json`，也不会触发扫描或 Process Lasso 规则。GamePP 来源数据不按本仓库的 CC0 游戏身份记录授权。

更新候选时，在 `gamedb` 目录运行 `D:/Anaconda3/envs/pytorch/python.exe tools/import-gamepp.py <GamePP0.dat路径>`。脚本只读数据库，选择 `WhiteBlack` 表中 `type=1` 且 `on_off=1` 的记录；仅保留有效 EXE 文件名，过滤可明确识别的启动器、编辑器、跑分程序、安装器、服务、重复 `.exe` 扩展名，以及同库已有原名的 `(2)` 等编号副本。无法仅凭文件名判断的条目继续保留为待审候选。

2026-10-26 的全库候选比对及证据审核结果见 `reviews/gamepp-type1-2026-10-26.md`。未证实的名称仍留在候选文件中。
