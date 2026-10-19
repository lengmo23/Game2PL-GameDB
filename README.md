# Game2PL GameDB

这个目录是社区游戏身份库的仓库原型。`records` 是可审查的数据源，`generated/gamedb-v1.json` 是客户端读取的生成物。

数据库事实记录采用 CC0-1.0，构建与校验脚本采用 MIT；详情见 `LICENSE-DATA` 和 `LICENSE-CODE`。

- `verified`：只有平台 ID 与本机安装证据同时匹配时才能参与识别。
- `pending`：不能进入发布索引，也不能触发 Process Lasso 写入。
- `rejected`：明确的非游戏，用于阻止误判。
- `deprecated`：被替换或合并的旧记录。

运行 `npm run build` 生成索引。正式拆分为独立 GitHub 仓库后，应由 GitHub Actions 校验记录、生成压缩索引并发布 Release；人工审核是从 `pending` 进入 `verified` 的必要条件。
