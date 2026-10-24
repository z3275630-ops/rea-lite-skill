# REA Lite Skill

中文 · [English](README.en.md)

**让 REA 少占上下文，工具用到再加载。**

我用 [REA](https://github.com/morluto/rea) 做逆向时，最受不了的一件事是：新对话刚打开，工具定义就占了约 **20 万 token**。

REA 有很多工具，但一次任务通常只需要其中一部分。我想把工具都留着，等用到时再让 AI 读取说明，不必每次都把整套工具定义塞进上下文。

于是做了 REA Lite Skill：通过按需加载的网关调用原版 REA，再把长手册拆成按任务阅读的参考资料。

## 能省多少

下面是 REA 6.7.0 的一次对比测试：

| | 原版直接连接 | REA Lite |
|---|---:|---:|
| 工具说明 | 约 18.7 万 token | **约 1,200 token** |
| 工具和技能说明合计 | 约 19.2 万 token | **约 2,400 token** |
| 可访问的 REA 工具 | 207 个 | **207 个** |

按同一方法计数，这部分开销减少了约 **98.7%**。这里只计算 REA 的工具、技能及相关触发说明；不同客户端的实际占用会有差异，后续分析产生的内容另计。[查看测量方法](docs/STARTUP.md)

## 改了什么

- **工具保留。** 实际分析仍由官方 REA 执行，原有分析引擎和运行条件不变。
- **说明按需读。** AI 先看到少量搜索和调用入口，需要某个工具时再读取它的参数。
- **手册更短。** 技能入口从约 23.5 KB 减到 4.6 KB，六份上游领域指南保留，按任务读取。

网关复用了 [MCP Compression Proxy](https://github.com/kdpa-llc/mcp-compression-proxy)。例如分析 APK 时，先读 Android 指南，再查找需要的工具；分析依然交给 REA 和相应引擎完成。

目前已逐项核对 207 个工具的参数，并完成一次离线调用对照。技能中的部分进阶说明经过精简，具体改动和测试范围见[验证记录](docs/REVIEW.md)。

## 开始使用

目前提供 ZCode 安装说明，使用 **REA 6.7.0 + MCP Compression Proxy 1.3.3**。

1. 将整个 `skills/reverse-engineer-anything/` 文件夹复制到 `~/.zcode/skills/`；已有同名技能请先备份。
2. 将 [snippets/AGENTS.md](snippets/AGENTS.md) 合并到自己的 `~/.zcode/AGENTS.md`。
3. 按[安装指南](docs/SETUP.md)配置按需网关，在该客户端关闭直连 REA，改为通过网关访问。
4. 重新连接客户端，开一个新对话，告诉 AI 目标文件的路径和你想分析的问题。

**需要同时配置网关；只复制技能文件，不会减少直连 MCP 的工具占用。** 其他客户端请按各自的 MCP 配置方式接入。

## 来源与许可

基于 [morluto/rea 6.7.0](https://github.com/morluto/rea) 修改的非官方技能，与上游没有隶属或背书关系。

MIT，保留 Copyright (c) 2026 morluto。

[LICENSE](LICENSE) · [NOTICE](NOTICE) · [更新记录](CHANGELOG.md)
