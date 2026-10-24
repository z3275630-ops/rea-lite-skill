# ZCode setup

This guide configures documentation plus a lazy gateway. It does not install
IDA, Ghidra, JADX, JEB or other analysis engines. Keep existing configuration
and back up the skill/config files before replacing or merging entries.

## 1. Prerequisites

Use an existing compatible Node.js. REA 6.7.0 declares
`^22.23.4 || ^24.22.1 || >=26.12.1`; use that package's actual engine requirement,
not a generic Node 22 claim. If package installation is desired:

```powershell
npm install -g rea-agents@6.7.0 mcp-compression-proxy@1.3.3
npm root -g
```

The second command prints your global npm module directory. Replace every
`<npm-global-root>` below with it; in JSON, use forward slashes (Windows accepts
them), or escape each backslash. These are placeholders, not runnable paths.
Using Node with the package entrypoint avoids Windows `.cmd` launcher ambiguity.

## 2. Configure the proxy backend

Merge the following into `~/.mcp-compression-proxy/servers.json` (create its
directory if needed). Preserve your unrelated servers and settings. This
example contains no credentials; never publish your actual configuration.

```json
{
  "toolExposure": "lazy",
  "backendMode": "local",
  "mcpServers": [
    {
      "name": "rea",
      "command": "node",
      "args": ["<npm-global-root>/rea-agents/scripts/rea.mjs", "--mcp"],
      "inheritEnv": true
    }
  ]
}
```

REA receives the proxy process environment with this example. Pass only the
provider variables you actually need if a narrower environment is desired;
the proxy supports an environment-name allowlist instead of `true`. Provider
settings remain local and no credentials are needed for the skill itself.

Project `./servers.json` also overrides proxy settings: inspect it if the
observed exposure differs. A nonempty `pinnedTools` setting can expose backend
schemas directly even in lazy mode. Do not pin the entire REA catalog.

## 3. Configure ZCode's gateway

Merge this server entry into ZCode's existing `~/.zcode/cli/config.json`, under
`mcp.servers`. Do not replace the rest of the file. If a direct `rea` entry
exists there, set its existing `enabled` field to `false`.

```json
{
  "mcp": {
    "servers": {
      "analysis-lazy": {
        "type": "stdio",
        "command": "node",
        "args": ["<npm-global-root>/mcp-compression-proxy/dist/index.js"],
        "timeoutMs": 180000
      }
    }
  }
}
```

`analysis-lazy` is the chosen registration name, not a REA command. Other
clients use their own MCP configuration format and tool-name prefixes.
Upstream `rea setup` can replace the skill and restore a direct REA entry;
review its dry-run instead of applying it blindly to this arrangement.

## 4. Install the skill and trigger snippet

Copy the entire `skills/reverse-engineer-anything` folder, including
`references`, into `~/.zcode/skills`. Merge [the snippet](../snippets/AGENTS.md)
into `~/.zcode/AGENTS.md`. Do not install only `SKILL.md`.

Restart/reconnect ZCode and start a new conversation. Existing conversations
may retain their original tool context. Give the full target path and question.

## 5. Verify

The client should see gateway discovery tools, not 207 individual REA tools.
Use the client's actual tool names (it may prefix or normalize them):

1. `mcp-compression-proxy__search_tools` with
   `{"query":"inspect_pe_resources","limit":5}`.
2. `mcp-compression-proxy__get_tool` with
   `{"server":"rea","tool":"inspect_pe_resources"}`.
3. `mcp-compression-proxy__call_tool` with
   `{"server":"rea","tool":"inspect_pe_resources","arguments":{"path":"<your-explicit-PE-path>"}}`.

This offline inspection does not execute the selected PE. Use a file you are
authorized to inspect. A successful Evidence response proves that one route;
it does not establish that IDA, JADX or every provider is configured.

The reference release check used a separate disposable home/configuration;
it did not overwrite a user's ZCode settings. See [REVIEW.md](REVIEW.md).

Sources: [proxy configuration](https://github.com/kdpa-llc/mcp-compression-proxy),
[REA 6.7.0 package metadata](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/package.json).
