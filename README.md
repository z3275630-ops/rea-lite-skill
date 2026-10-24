# REA Lite Skill

**About 80% smaller skill entrypoint. All 207 REA tool schemas remain accessible.**

An unofficial, on-demand skill for [REA](https://github.com/morluto/rea),
derived from **morluto/rea 6.7.0**. It helps agents reverse engineer APKs,
native binaries, .NET, Electron/JavaScript bundles, firmware and captures
without loading every provider guide and tool schema at the start.

## What gets lighter

| Measured item | Upstream / direct | REA Lite / lazy |
|---|---:|---:|
| Skill entrypoint, UTF-8 bytes | 23,523 | **4,630 (-80.3%)** |
| Skill entrypoint, `o200k_base` tokens | 5,071 | **1,036 (-79.6%)** |
| Client-facing tool entries | 207 REA tools | **9 gateway tools** |
| Serialized MCP catalog, UTF-8 bytes | 3,158,368 | **4,879 (-99.85%)** |

These are two separate improvements: a shorter skill entrypoint and lazy MCP
discovery. **Copying this skill alone does not configure the gateway or remove
an existing direct REA registration.** Reference files and selected tool schemas
load later when needed; the savings are not a promise about total task tokens.
Catalog size includes complete `tools/list` JSON; clients may transform or omit
parts before prompting. See the [measurement method](docs/REVIEW.md).

## What stays available

- Target routing, schema-first calls, evidence IDs, bounded paging and cleanup.
- Provider constraints and practical recipes, loaded only for the task at hand.
- All **207 exact REA 6.7.0 tool names** and their original input schemas.
- Six upstream domain guides, retained byte-for-byte with MIT attribution.

REA Lite changes documentation and connection guidance. It does not fork the
analysis backend or bundle engines. Each operation still needs its supported
host, provider, configuration and authorization. All 207 schemas were verified
through the gateway; one offline PE inspection returned identical Evidence
through direct and lazy connections. This does not certify all 207 operations
against real engines.

## Install in ZCode

1. Have a compatible Node.js, `rea-agents@6.7.0`, and
   `mcp-compression-proxy@1.3.3` installed.
2. Back up an existing skill, then copy `skills/reverse-engineer-anything/`
   into `~/.zcode/skills/`. Keep the folder name `reverse-engineer-anything`.
3. Merge [snippets/AGENTS.md](snippets/AGENTS.md) into your existing
   `~/.zcode/AGENTS.md`; preserve unrelated instructions.
4. Configure the proxy with **`toolExposure: "lazy"`** and a `rea` backend.
   Register only the gateway in this client; disable its direct REA entry.
5. Start a new conversation. Ask a concrete artifact question and verify
   search → schema lookup → call through the gateway.

The [complete setup guide](docs/SETUP.md) includes portable JSON examples and
Windows paths. No private configuration files are distributed here.

## Compatibility and layout

Pinned to **REA 6.7.0** and tested with **MCP Compression Proxy 1.3.3**, Windows
x64 and Node.js. ZCode discovery is the primary installation target. Other
clients can load the same skill if they support skills and lazy MCP; use their
actual tool prefixes and configuration format. Re-check behavior after upgrades.
The agent must have an ordinary file-reading tool to load reference files.

```text
skills/reverse-engineer-anything/
  SKILL.md                 # small entrypoint
  references/              # load only the relevant guide
snippets/AGENTS.md          # Chinese trigger rules
docs/SETUP.md               # installation and configuration
docs/REVIEW.md              # findings, evidence and verification limits
docs/tool-names-6.7.0.txt    # exact backend inventory
LICENSE / NOTICE           # upstream attribution
```

## 中文说明

这是 REA 的非官方轻量技能：入口正文约减少 **80%**，通过懒加载网关按需读取
工具参数，保留 207 个工具的访问路径。只安装技能不会自动完成网关配置。
引擎、平台和授权限制仍然适用；“保留工具访问能力”不代表实测了全部工具。

## Attribution and license

Derived from [morluto/rea](https://github.com/morluto/rea), **6.7.0**, MIT,
Copyright (c) 2026 morluto. **Not affiliated with or endorsed by the REA project.**
[MCP Compression Proxy](https://github.com/kdpa-llc/mcp-compression-proxy)
is a separate dependency. See [LICENSE](LICENSE), [NOTICE](NOTICE) and
[CHANGELOG.md](CHANGELOG.md).
