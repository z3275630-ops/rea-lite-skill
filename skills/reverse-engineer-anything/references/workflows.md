# Investigation workflow and recipes

## 4. Standard investigation loop

1. **Checklist.** Turn the request into questions; for each, name the evidence type that can answer it. Resolve target identity from the conversation/workspace before asking again.
2. **Smallest overview.** `open_binary` / `inspect_*` / `analyze_*`, selecting `detail: "summary"` only where the advertised schema supports it. Do not start with a complete graph or all strings.
3. **Read the envelope.** Note `evidence_id`, `parent_evidence_id`, provider, `analysis_profile`, coverage, limitations, unknowns. If the result is a preview, page the retained parent instead of re-running.
4. **Drill.** `inspect_analysis_view` with summary → section → item/page. For JS graphs, page module identities and select a `node_id` before requesting an item. For native, use `procedure_pseudo_code`, `procedure_assembly`, `xrefs`, `get_call_graph` only where a specific question needs them.
5. **Expand only on a concrete gap.** Batch related calls around one hypothesis. Do not repeat an identical analysis or a rejected call without a changed input or resolved blocker.
6. **Corroborate.** Use runtime/browser/Electron/Android observation only when static evidence cannot answer, and only within the declared target and actions.
7. **Ledger + close.** Keep conclusion → evidence ID → observed/inferred/unknown → boundary. Revisit the checklist; mark answered / partial / unresolved. `close_binary`.

## 7. Evidence model and output contract

- Evidence-producing operations return an `evidence_id` (content-addressed, `ev_` prefix) and often a `parent_evidence_id`.
- Large analyses are retained in the ledger. `inspect_analysis_view` reads summary, one section/module, or a stable page. `retention: "complete-record"` means the whole record is stored; native value-flow truncation and unknown metadata remain separate facts.
- `get_evidence_bundle` with `detail: "summary"` and exact filters finds retained analysis when the parent ID is unknown. `export_evidence_bundle` writes a portable bundle; `import_evidence_bundle` reads one.
- `list_unknowns` / `record_unknown` / `update_unknown` / `verify_unknown_resolution` maintain the explicit unknown set. Use them instead of silently dropping gaps.
- A "resource_constraint" with `details.resource: "transport"` means the response was too large: use `inspect_analysis_view` on the reported same-session reference, or export the bundle. Do not repeat the producer merely to get the same oversized response.
- Static analysis never proves execution. A string, name, or filename is not behavior. Distinguish observations, inferences, and unknowns; preserve coverage limits and bounded negative results.

Recommended report shape:

```
Question:
Target + digest:
Provider / profile:
Findings: <claim> [evidence_id] (observed|inferred)
Unknowns / partial coverage:
Next steps:
```

## 10. Recipes

**APK static triage.** `inspect_android_package` → `decode_android_resources` → `search_android_classes` / `inspect_android_class` → `inspect_android_method` → `trace_android_references`. Cite package digest and split set.

**Native decompile.** `open_binary` → `binary_overview` when supported (skip it for IDA) → `search_procedures` / `search_strings` → `procedure_pseudo_code` / `procedure_assembly` → `xrefs` / `procedure_callers` → ledger → `close_binary`.

**Electron feature trace.** `analyze_javascript_application` with summary → page module identities → `trace_application_feature` → `inspect_analysis_view` for the selected node → corroborate with `capture_electron_scenario` only if needed.

**Version diff.** Analyze both artifacts (summary) → `compare_application_versions` / `compare_functions` / `find_changed_behavior` → report each change with both evidence IDs and the comparison boundary.

**Protocol / PCAP.** `inspect_pcap_capture` summary → `inspect_packet_fields` for field names/types → `inspect_packet_capture` with selected fields and display filters → page frames; preserve the source digest.

**Managed .NET.** `inspect_managed_artifact` → `inspect_managed_members` → `compare_managed_members` when diffing → `inspect_managed_native_boundaries` for NativeAOT edges.

**JEB.** `inspect_jeb_client` → `list_jeb_units` → `decompile_jeb_item` for an existing project. Use `open_jeb_project` only when the engine advertises project opening and selecting a new project is authorized. An optional separately configured `server: "jeb"` can expose additional native tools; inspect its schemas first.
