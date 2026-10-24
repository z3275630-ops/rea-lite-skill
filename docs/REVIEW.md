# Release review: v1.0.0

**PASS** after the corrections below. No unresolved publication blockers were
found in the release files. This is a documentation release, not a certification
of every REA provider.

## Findings and disposition

Locations in this table refer to the submitted ZIP before this review. `SKILL`
means `skills/reverse-engineer-anything/SKILL.md`.

| File:line | Severity | Finding | Final disposition |
|---|---|---|---|
| README.md:3; docs/CHANGES.md:4 | major | The claimed 28,662-byte official baseline was not reproduced from the pinned release. | Use the verified authored and generated source sizes below. |
| README.md:15; SKILL:15 | major | A fixed 192k-token startup claim mixed schema estimates with actual client prompting. | Measure serialized catalog bytes and document tokenizer and client boundaries. |
| references/tool-index.md:3 | major | The grouped index claimed 207 tools but contained 191 distinct names. | Add the missing 16; the final index exactly matches the 207-name inventory. |
| SKILL:37 | major | The client-specific MCP prefix was treated as a portable tool identifier. | Use the actual advertised proxy names and explain client prefixes. |
| SKILL:43-48,118 | major | Local JEB catalog/launcher/session assumptions were presented as general setup. | Document the upstream default port, optional JEB backend and operator-supplied service; remove the absent private launcher. |
| SKILL:99,172 | major | The general recipe could add unsupported summary arguments or request IDA's unavailable overview. | Obtain the live schema, use summary conditionally, and skip IDA overview. |
| docs/CHANGES.md:20 | major | The change summary called Kuna coverage Linux-only. | Confirm Linux and macOS adapter support; Windows remains unsupported. |
| SKILL:110-130 | major | Provider details remained in the shared entrypoint. | Move them to a task-specific reference, retaining constraints and recipes. |
| NOTICE:17; README.md:28 | minor | All reference files were described as upstream although the tool index was custom. | Name the six verbatim upstream files; distinguish additions and adaptations. |
| .gitignore:1-8 | minor | Private proxy/client files, package archives and payload directories were not explicitly excluded. | Add exclusions and inspect the complete staged tree independently. |
| snippets/AGENTS.md:4 | minor | The trigger required a Skill tool and could attract ordinary source-version comparisons. | Add file-reading fallback and restrict triggering to shipped-artifact questions. |

The submitted frontmatter was already valid YAML. Its quoted description was
retained as valid frontmatter and revised for concise bilingual discovery.

## Sources and size method

Upstream tag: `rea-agents-6.7.0`, commit
`27dc42d10249f0410904a75c0997842eb03b931c`.

- [Authored skill](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/.agents/skills/reverse-engineer-anything/SKILL.md):
  23,510 UTF-8 bytes.
- [Package generator](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/scripts/generate-skill-metadata.mjs):
  add `tool_count: 207` and pin `rea-agents@latest` to `rea-agents@6.7.0`.
  Reconstructed generated skill: 23,523 bytes; it matched the installed 6.7.0
  package entrypoint byte-for-byte. SHA-256:
  `fbcd39d6abe803cf7aa49c1880815bc8e22ba2af87a23681944f687bb7629eb1`.
- Submitted entrypoint: 16,204 bytes / 3,906 tokens.
- Final entrypoint: **4,630 bytes / 1,036 tokens**, measured on complete UTF-8
  file content including frontmatter. This is 80.3% fewer bytes / 79.6% fewer
  tokens than the generated upstream baseline, and 71.4% fewer bytes / 73.5%
  fewer tokens than the submitted entrypoint.

Token counts use `tiktoken` with `o200k_base`; other models and client framing
differ. The archived local 28,662-byte file is not the official comparison
baseline. Measurements are also available in [measurements.json](measurements.json).

## Runtime and schema verification

On Windows x64, start fresh local stdio processes with a disposable home and
proxy configuration. Do not use a user's credentials or edit their ZCode setup.
Initialize MCP, fetch all `tools/list` pages, and serialize the catalog as
`JSON.stringify({tools})` without whitespace.

| Connection | Tool entries | UTF-8 bytes | `o200k_base` tokens |
|---|---:|---:|---:|
| REA 6.7.0 default catalog | 207 | 3,158,368 | 833,082 |
| REA 6.7.0 compact input profile | 207 | 2,576,431 | 689,701 |
| Proxy 1.3.3, explicit lazy exposure | 9 | 4,879 | 1,128 |

These count the complete wire catalog, including output schemas and other
metadata. They are not measurements of a particular client's system prompt.
The compact input profile still returned output schemas in this configuration;
it should not be confused with lazy exposure. Proxy settings, pinned tools,
additional backends and future versions can change the result.

The test host used Node.js **26.7.0**. This is below REA 6.7.0's declared
26.x floor (`>=26.12.1`); the observed checks passed, but this does not establish
support for that older runtime. Install using the supported package range
documented in [SETUP.md](SETUP.md).

Checks performed:

1. Compare the packaged `TOOL_CONTRACTS` inventory with the supplied tool-name
   list: exactly 207, no additions, omissions or duplicates.
2. Fetch all 207 `get_tool` results through the lazy gateway. Every original
   input schema equals the corresponding direct REA `tools/list` schema.
3. Find `inspect_pe_resources` through `search_tools`, read its schema, and
   invoke it through `call_tool` on a standard Windows PE file without executing
   it. The complete returned Evidence, including its ID and normalized result,
   equals the direct-call Evidence.
4. Compare all six retained reference guides against the pinned GitHub source:
   byte-for-byte equal. Preserve the complete upstream MIT text and copyright.
5. Validate frontmatter and naming with the skill validator; verify relative
   links and inspect linked upstream document paths.

No IDA/JEB/native debugger attach, device mutation, arbitrary target execution
or 207-operation real-engine test was performed. Tool schema preservation does
not establish provider installation or identical agent reasoning. Fresh ZCode
model-driven skill selection was not exercised during this release review.

## Provider checks

The following were checked against the pinned documentation/source rather than
inferred from tool names:

- [IDA](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/docs/ida-provider.md):
  original binary input, attached/headless ownership and unavailable overview.
- [JEB](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/docs/jeb-analysis.md):
  default 8425 endpoint, validated override, operator-owned service and optional
  project-opening support.
- [JADX](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/src/android/JadxConfiguration.ts):
  `REA_JADX_OPERATION_TIMEOUT_MS` and the 120,000 ms default.
- [Kuna](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/docs/kuna-provider.md):
  Linux/macOS support, Windows and target-format exclusions.
- [Packet fields](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/docs/packet-captures.md)
  versus [PCAP summary](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/docs/pcap-analysis.md):
  distinct Linux prlimit and Windows Job Object host boundaries.
- [Electron fuses](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/docs/electron-fuses.md)
  and [ADB](https://github.com/morluto/rea/blob/27dc42d10249f0410904a75c0997842eb03b931c/src/adb/AdbProvider.ts):
  Inspector fuse behavior, explicit serial use and fresh package subdirectory
  for base/split pulls.

## Privacy, license and publication boundary

Inspect every release file as text and scan for credential formats, private
keys, Bearer values, personal paths/usernames, device identifiers, email
addresses and private IP ranges. The documented `127.0.0.1:8425` endpoint is a
generic loopback default, not a private service disclosure. SHA-256 values in
measurements are public file digests, not credentials.

Publish an explicitly enumerated tree from its own `.git` directory. The tree
contains no `config.json`, `servers.json`, `.zcode`, logs, payloads,
`node_modules`, npm tarball, installed package, engine or binary. JSON settings
appear only as placeholder examples inside documentation. A final archive is
constructed from committed files, excluding `.git` and all test artifacts.

MIT is retained in full with `Copyright (c) 2026 morluto`. `NOTICE` identifies
the derivative, custom references and changes. The `rea-lite-skill` name and
README explicitly identify the project as unofficial. No separate SECURITY
policy was added for this documentation-only release; ordinary reports can
use repository issues, without posting secrets.
