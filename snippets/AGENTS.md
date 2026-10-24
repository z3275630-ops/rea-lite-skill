<!-- rea:begin -->
## 逆向 / 反编译任务

当问题依赖已发布产物（APK/IPA、原生或 .NET 二进制、ASAR、固件、抓包、
WASM/EVM、SQLite）或要求反编译、脱壳、解包、追踪产物行为、比较发布版本、
恢复协议时，在首次 REA 调用前加载 `reverse-engineer-anything` 技能。
若客户端没有 Skill 工具，读取该技能的 `SKILL.md`；只按当前任务加载参考文件。
普通源码分析不触发。通过配置了 `toolExposure: "lazy"` 的 `analysis-lazy`
网关访问 `rea`，先搜索、读取参数定义，再调用；不要启用直连 REA MCP。
未连接时先检查配置，技能安装本身不会注册网关。保留用户的授权和目标范围。
<!-- rea:end -->
