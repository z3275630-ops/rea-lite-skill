# Startup context comparison

The author encountered roughly 200k tokens of overhead in a direct-REA client
setup. That is a personal observation, not a universal REA startup cost.
The README comparison uses the following separately reproducible measurement.

## Fresh captures and normalization

On 2026-10-24, start isolated REA 6.7.0 and MCP Compression Proxy 1.3.3 processes,
with a disposable home and a proxy configuration explicitly setting
`toolExposure: "lazy"`, one `rea` backend, and no pinned tools. Initialize MCP
and collect every `tools/list` page into `{"tools":[...]}`. The observed counts
are 207 and 9, respectively. No user credentials or current-client changes are
needed for this catalog inspection.

For each tool, keep its name, description and input schema in a normalized
function declaration:

```json
{
  "type": "function",
  "function": {
    "name": "<original name>",
    "description": "<original description>",
    "parameters": {"<original input schema>": "unchanged"}
  }
}
```

This is a counting representation, not a request to change the MCP protocol.
Serialize the array as compact UTF-8 JSON, with non-ASCII characters retained.
Count it with [tiktoken](https://github.com/openai/tiktoken) 0.12.0 and
`o200k_base`. **Do not include outputSchema or unrelated wire metadata** in
this particular model-facing comparison. Those are covered by the separate
full-wire measurements in [REVIEW.md](REVIEW.md).

## Results and arithmetic

| Component | Direct REA | Lazy gateway |
|---|---:|---:|
| Function-definition JSON bytes | 779,369 | 5,139 |
| Function-definition tokens | 186,725 | 1,171 |
| Loaded skill tokens | 5,071 | 1,036 |
| Added AGENTS trigger snippet | 0 | 200 |
| Combined comparison budget | **191,796** | **2,407** |

Direct: `186725 + 5071 = 191796`.
Lite: `1171 + 1036 + 200 = 2407`.
Reduction: `1 - 2407 / 191796 = 98.745%`, rounded to **about 98.7%** in the README.
The direct baseline does not add a trigger snippet that upstream does not ship.
The Lite budget includes the complete supplied snippet, including its comments.

The upstream generated entrypoint has the same SHA-256 recorded in REVIEW.md;
the Lite skill entrypoint is unchanged from v1.0.0/v1.0.1. Raw catalogs are not
committed because the release deliberately avoids bundling complete backend
schemas and local capture files. Summary data is in
[startup-measurements.json](startup-measurements.json).

## Recount saved captures

The optional helper only needs Python and `tiktoken`. Use existing tooling or
install `tiktoken==0.12.0` in your preferred environment. Save the direct and
lazy catalogs and the official generated REA 6.7.0 skill to local files, then:

```text
python scripts/count_startup_tokens.py --direct direct-catalog.json --lazy lazy-catalog.json --upstream-skill upstream-SKILL.md
```

The script reads the current repository's skill and trigger snippet and prints
counts without exposing raw tool definitions or personal file paths. It counts
the provided captures; it does not launch engines, capture your client's actual
system prompt or make model API requests. Its fixed release metadata refers to
this 6.7.0/1.3.3 experiment, so use the corresponding versions when reproducing it.

## Interpretation and limits

- The combined number is a **REA-related comparison budget after skill
  activation**, not an observed total fresh-chat context or billing measurement.
  Before activation, the 1,036-token skill body is not loaded.
- It excludes client system prompts, unrelated tools/skills, messages, extra
  protocol framing and possible duplicate skill discovery metadata. A client can
  transform declarations and add its own overhead; different tokenizers differ.
- Reading a reference, fetching a tool schema or returning analysis results
  consumes more context later. The estimate is not the total task cost.
- This does not benchmark an actual ZCode conversation. Existing client-native
  discovery can substantially reduce the direct baseline already.
- The 207 unchanged tool schemas and one identical PE Evidence round trip are
  documented in REVIEW.md. They do not prove equal end-task quality across all
  providers or offset condensed specialized instructions.
