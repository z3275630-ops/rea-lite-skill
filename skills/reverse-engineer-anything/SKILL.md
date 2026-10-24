---
name: reverse-engineer-anything
description: 'Reverse engineer shipped APK/IPA, native and .NET binaries, Electron/JavaScript bundles, firmware, packet captures, WASM/EVM and SQLite with REA. Use for decompiling, unpacking, tracing behavior, comparing shipped versions or recovering protocols; also 逆向、反编译、脱壳、解包、抓包、协议分析. Skip ordinary source-repository analysis.'
metadata:
  version: "1.0.0"
  upstream: "rea-agents@6.7.0"
  tool_count: "207"
---

# REA Lite Skill

Read this before the first REA call. Load only the reference needed for the
current target; never preload the complete catalog or all guides.

## First steps

1. Resolve the user's actual artifact or runtime target and question. Use normal
   source tools when a checkout answers it. If the target cannot be resolved,
   ask once; never substitute an example application.
2. Use the lazy MCP gateway (conventionally `analysis-lazy`), with backend
   `rea` and `toolExposure: "lazy"`. Keep direct REA registration disabled in
   this client. If the gateway is absent, read [gateway.md](references/gateway.md)
   and diagnose configuration; installing the skill alone does not connect it.
3. `search_tools` → `get_tool` → `call_tool`. Select the client's advertised
   gateway tool names. Pass `server: "rea"` and the exact REA `tool`; obtain its
   real argument schema and effects before calling. Never guess parameters.
4. Start with the smallest relevant overview. Use `detail: "summary"` only when
   supported by that tool's schema. Follow retained evidence with bounded pages
   through `inspect_analysis_view`; do not rerun a producer to browse its output.

## Choose a route

| Target / question | Start with | Read when needed |
|---|---|---|
| Native binary | `open_binary`; overview if supported | [Native](references/native-and-artifacts.md), [providers](references/provider-notes.md) |
| APK code / resources | `inspect_android_package` / `decode_android_resources` | [Android](references/android-applications.md) |
| .NET assembly | `inspect_managed_artifact` | [Managed](references/native-and-artifacts.md) |
| ASAR / shipped JS / web bundle | `analyze_javascript_application` / `analyze_web_bundle` | [JavaScript](references/javascript-applications.md) |
| Existing browser / Electron runtime | `list_browser_targets` / `list_electron_targets` | [Runtime](references/runtime-observation.md) |
| Archive / application package inventory | `open_binary` → `inspect_artifact` | [Packages](references/native-and-artifacts.md) |
| PCAP, firmware, WASM/EVM, SQLite, Go/Rust metadata, other formats | Select the specific offline inspector | [Detailed routing](references/routing.md), [providers](references/provider-notes.md) |
| Comparison / evidence / reconstruction | Reuse the relevant existing Evidence | [Evidence](references/evidence-workflows.md), [recipes](references/workflows.md) |

Read [provider-notes.md](references/provider-notes.md) before provider-specific
setup or after a provider failure. IDA takes the original binary, not `.idb` /
`.i64`, and has no `binary_overview`. Offline Android code inspection does not
require opening a native session. JEB is optional and uses an operator-supplied
service. For an uncovered tool family, search or read the complete
[207-name index](references/tool-index.md) on demand.

## Evidence, scope and cleanup

- Cite returned `evidence_id` values for REA findings; preserve parent IDs,
  artifact digests, provider/profile, coverage, limitations and unknowns.
  Distinguish observed / inferred / unknown. Ordinary shell checks are their own
  source, not REA Evidence. Static names and strings do not prove execution.
- Follow `normalized_result.parent_evidence_id` when a summary wraps retained
  analysis. If a preview is truncated or saved as a gateway payload, page the
  retained output; see [gateway.md](references/gateway.md). A partial negative
  search or exhausted page does not prove global absence.
- Runtime actions, device changes and annotations require the user's authorized
  scope. Inspect effects before executing; preserve existing projects and device
  selection. Do not install or reconfigure unrelated providers to clear a gap.
- Keep a question → evidence → conclusion → remaining-gap ledger. Expand only
  to resolve a concrete gap; do not repeat an unchanged failed or rejected call.
- Export needed session evidence before `close_binary`, which clears retained
  references. Close native / Frida / debugger sessions that you opened when done.
  Read [workflows.md](references/workflows.md) for investigation recipes.
