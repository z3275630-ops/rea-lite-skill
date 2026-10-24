# Lazy gateway and recovery

Read this for gateway names, payload paging or an observed connection failure.
The proxy configuration must explicitly set `toolExposure: "lazy"`. The
`analysis-lazy` server name is a local convention; use the name and tool prefix
actually advertised by the client. Installation alone does not configure MCP.

## Discover, inspect, call

The proxy's actual MCP names are `mcp-compression-proxy__search_tools`,
`mcp-compression-proxy__get_tool` and `mcp-compression-proxy__call_tool`.
A client may prepend its server identifier or normalize punctuation. Select
the tools exposed in the current session rather than hard-coding a prefix.

1. `search_tools`: an exact tool name or concise English keywords; begin with
   a small `limit`. Ranked search is not a complete inventory; refine it if missing.
2. `get_tool`: `{"server":"rea","tool":"<exact name>"}`. Read the input schema,
   description, effects and annotations before the first call.
3. `call_tool`: `{"server":"rea","tool":"<exact name>","arguments":{...}}`.
   `want` / `where` optionally narrow output; do not remove evidence identity,
   coverage or limitations needed to support a conclusion.

The proxy also exposes `read_output` and `find_output`. Oversized results may
be retained as local payloads (default threshold in proxy 1.3.3: 10,000
characters; configurable). A preview is incomplete: search or read bounded
pages, for example `length: 8000`; do not request `all: true` just to browse.
Read each gateway tool's live schema before using its arguments.

## Recover only the failing layer

- No gateway tools: inspect this client's gateway configuration and reconnect
  or start a fresh conversation. Do not add a direct REA registration.
- Gateway present but REA missing: check the configured `rea` backend and its
  launch diagnostic. Consult the [public setup guide](https://github.com/z3275630-ops/rea-lite-skill/blob/v1.0.0/docs/SETUP.md).
- Unknown provider readiness: use `binary_session` with `{}` once and inspect
  `result.tool_availability`. A catalog of 207 names does not prove 207 available
  operations. A provider failure affects the route that needs it.
- Diagnose an installed CLI with `rea doctor --client zcode --json`; if no CLI
  exists, acquiring `npx -y rea-agents@6.7.0` must be in the authorized scope.
  `npx` may download a package and write npm's cache.
- Inspect `rea setup --client zcode --dry-run --json` before any repair.
  Applying upstream setup can restore a direct REA registration and replace
  this skill: retain the lazy gateway arrangement and inspect the exact changes
  before applying authorized writes. Do not install analysis engines to repair
  registration. For other clients, substitute the actual supported client ID.
- For JEB, use the operator's installed MCP service; see
  [provider-notes.md](provider-notes.md). No bundled launcher is assumed.

The [upstream recovery guide](connection-and-recovery.md) contains optional
direct-registration examples. They describe upstream operation; do not copy
them into this lazy setup. Preserve client approvals and target scope.
