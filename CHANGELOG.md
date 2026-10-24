# Changelog

## v1.0.2 - 2026-10-24

- Rewrite the README around the author's ~200k-token startup experience, with
  Chinese as the primary version and an English translation.
- Add a fresh model-facing comparison: 191,796 to 2,407 REA-related tokens
  including the loaded skill and trigger snippet, about 98.7% lower under the
  documented normalization. This is not a client's total prompt measurement.
- Add measurement JSON, an optional token-counting helper and reproduction
  instructions. Distinguish 207/207 tool-interface preservation from unproven
  task-quality equivalence and condensed specialized guidance.
- The skill entrypoint, backend, tool interfaces and license are unchanged.

## v1.0.1 - 2026-10-24

- Keep LICENSE byte-for-byte identical to upstream MIT and move the additional
  modification copyright notice to NOTICE for GitHub license recognition.
- Skill content, measurements and all tool schemas are unchanged.

## v1.0.0 - 2026-10-24

- First public release, derived from REA 6.7.0 under MIT.
- A 4,630-byte on-demand entrypoint, 80.3% smaller than the verified generated
  upstream skill; all six upstream domain guides retained.
- Complete 207-tool name inventory and identical input schemas through the
  tested lazy gateway; one offline PE Evidence round trip matched exactly.
- ZCode installation examples, Chinese AGENTS trigger, provider notes,
  measurement details and release review.

Tested with REA 6.7.0 and MCP Compression Proxy 1.3.3. Full provider runtime
coverage is not claimed.
