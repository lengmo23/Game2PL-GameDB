# GamePP type=1 启用项审核（2026-10-26）

## 范围与方法

- 来源：GamePP 5.6.70.519 的 `GamePP0.dat` / `WhiteBlack`，`type=1`、`on_off=1`；源文件 SHA-256：`31a927390535ae67760cdd468fb0a9f8ddcea3f01f4c32ee66465a8bdb61b387`。
- 24,149 条源行经过名称去重和已记录的明显非游戏过滤后，形成 `candidates/gamepp-type1.json` 的 23,116 个候选 EXE 名称；1,005 个被排除的名称及原因也保存在该文件中。源行数不是候选数与排除数之和，因为源表有重复名称。
- 对全部 23,116 个候选逐一做大小写无关的精确名称比对，检查它们是否与当前 `verified` 记录的主 EXE 对应。名称命中只用于定位待查对象，不构成独立证据。对本次升级的条目另行核对官方平台身份、官方发行商资料及主程序；缺少这种证据的名称继续保留候选。
- 本次没有把候选文件整体并入客户端索引。`generated/gamedb-v1.json` 只包含正式记录；候选名称不能单独触发本机游戏识别或 Process Lasso 规则。

## 本次新增的 verified 记录

| 记录 | GamePP 候选 EXE | 依据 |
| --- | --- | --- |
| `steam:1418630` Dread Hunger | `DreadHunger-Win64-Shipping.exe` | [Steam 商店](https://store.steampowered.com/app/1418630/Dread_Hunger/)与本机 `appmanifest_1418630.acf`、安装目录中的 Win64 客户端；排除同目录的 WindowsServer 与 UnrealCEF 子进程。 |
| `steam:1172470` Apex Legends | `R5Apex.exe` | [Steam 商店](https://store.steampowered.com/app/1172470/Apex_Legends/)与 [EA 支持文档](https://help.ea.com/en/articles/apex-legends/error-codes/)给出的 `r5apex.exe`。 |
| `steam:1091500` Cyberpunk 2077 | `Cyberpunk2077.exe` | [Steam 商店](https://store.steampowered.com/app/1091500/Cyberpunk_2077/)与 [CD PROJEKT RED 支持文档](https://support.cdprojektred.com/en/cyberpunk/pc/sp-technical/issue/1568/contact-to-support)给出的 `bin/x64/Cyberpunk2077.exe`。 |
| `steam:1174180` Red Dead Redemption 2 | `RDR2.exe` | [Steam 商店](https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/)与 [Rockstar 支持文档](https://support.rockstargames.com/articles/7n3mPnDq5ld6M6KIXboneC/red-dead-redemption-2-on-pc-crashing-with-err-gfx-state-error)给出的游戏 EXE。 |
| `standalone:fortnite` Fortnite | `FortniteClient-Win64-Shipping.exe` | [Epic 性能设置说明](https://www.epicgames.com/help/c-34254770/c-38015632/pcfortnite-a25544495)指出该游戏进程；[Epic 路径说明](https://www.epicgames.com/help/c-32735058/c-37477814/a10628872)列出它与单独的 Launcher、BE、EAC 文件。 |
| `standalone:league-of-legends` League of Legends | `league of legends.exe` | [Riot 支持文档](https://support-leagueoflegends.riotgames.com/hc/articles/43435443937299)给出 `Game/League of Legends.exe`，并分别列出 League Client 与 Riot Client。 |

## 覆盖结果与边界

- 当前所有 `verified` 记录的主 EXE 在候选中命中 **17 个名称**，包括本次新增的 6 个及此前已有的 11 个。大小写差异按 Windows 文件名处理。名称命中不代表该 GamePP 行已独立证实为某款游戏。
- **23,099 个候选名称仍未与现有 `verified` 主 EXE 名称命中**，全部继续留在 `candidates/gamepp-type1.json`；这组中可能有游戏、改名版本、启动器、工具或伪造名称。仅凭来源列表无法逐一确定其真实身份，因此本次不将它们批量批准或拒绝。
- 本次没有修改本机 Process Lasso 配置。`standalone` slug 仅是 GameDB 身份标识，不代表客户端可以仅凭同名 EXE 自动发现游戏。
