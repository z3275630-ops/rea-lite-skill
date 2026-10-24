# REA Lite Skill

[中文](README.md) · English

**Keep REA's tools. Load their definitions when you need them.**

When I used [REA](https://github.com/morluto/rea) for reverse engineering, one thing kept bothering me: a new chat in my setup started with roughly **200k tokens** taken up by tool definitions.

REA has a lot of tools, but most investigations only need a few of them. I wanted to keep the tools and let the AI read their instructions when needed, instead of loading the entire catalog at the start.

REA Lite Skill does that through a lazy gateway to the original REA backend, with a shorter skill entrypoint and reference guides read as needed.

## How much does it save?

One comparison using REA 6.7.0:

| | Direct REA connection | REA Lite |
|---|---:|---:|
| Tool definitions | ~187k tokens | **~1,200 tokens** |
| Tool and skill instructions combined | ~192k tokens | **~2,400 tokens** |
| Accessible REA tools | 207 | **207** |

Using the same counting method, this part of the context is about **98.7% smaller**. The figures cover REA tool definitions, the loaded skill and related trigger instructions. Actual client overhead varies, and later analysis adds more context. [Measurement method](docs/STARTUP.md)

## What changes?

- **Keep the tools.** The official REA backend still performs the analysis, using its existing engines and requirements.
- **Read definitions on demand.** The AI starts with a small set of discovery and calling tools, then reads the parameters for the tool it needs.
- **Use a shorter manual.** The skill entrypoint goes from about 23.5 KB to 4.6 KB. Six upstream domain guides are retained and read when relevant.

The gateway uses [MCP Compression Proxy](https://github.com/kdpa-llc/mcp-compression-proxy). For an APK investigation, for example, the AI reads the Android guide and finds the relevant tools; REA and its analysis engine still do the work.

All 207 input schemas have been checked, along with one offline call comparison. Some advanced instructions in the skill have been condensed. See the [verification notes](docs/REVIEW.md) for the changes and test coverage.

## Get started

The installation guide covers ZCode with **REA 6.7.0 + MCP Compression Proxy 1.3.3**.

1. Copy the entire `skills/reverse-engineer-anything/` folder into `~/.zcode/skills/`. Back up an existing skill with the same name first.
2. Merge [snippets/AGENTS.md](snippets/AGENTS.md) into `~/.zcode/AGENTS.md`.
3. Follow the [setup guide](docs/SETUP.md) to configure the lazy gateway and replace this client's direct REA connection with the gateway connection.
4. Reconnect, start a fresh chat and give the AI your target file's path and investigation question.

**Configure the gateway as well: copying the skill alone will not reduce a direct MCP connection's tool overhead.** Other clients need their own MCP configuration format.

## Attribution and license

An unofficial skill derived from [morluto/rea 6.7.0](https://github.com/morluto/rea). Not affiliated with or endorsed by the upstream project.

MIT, Copyright (c) 2026 morluto.

[LICENSE](LICENSE) · [NOTICE](NOTICE) · [Changelog](CHANGELOG.md)
