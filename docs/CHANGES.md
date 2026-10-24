# Changes from REA 6.7.0

Source: morluto/rea at `27dc42d10249f0410904a75c0997842eb03b931c`.

- Condensed the shared skill entrypoint to 4,630 UTF-8 bytes / 1,036
  `o200k_base` tokens; route and provider details are loaded on demand.
- Preserved six upstream reference guides byte-for-byte. Added focused
  gateway, routing, provider and workflow guides instead of removing domain
  documentation or changing the REA backend.
- Kept all 207 exact backend tool names and verified their gateway input
  schemas against direct `tools/list` results.
- Added the Chinese AGENTS trigger, a complete tool index and portable ZCode
  setup instructions. The index includes the 16 names omitted by the submitted
  grouped index.
- Corrected local JEB launcher assumptions, optional native-JEB catalog claims,
  Kuna's macOS support, schema-conditional summary requests and the IDA recipe.
- Replaced unqualified token estimates with measured sizes and explicit scope.
  The 28,662-byte archived local manual is not used as the official baseline;
  the pinned authored skill is 23,510 bytes and the generated package entrypoint
  is 23,523 bytes. See REVIEW.md for hashes and method.
- Added privacy exclusions and precise attribution for custom reference files.

The backend, provider implementations and execution boundaries are unchanged.
No analysis engines, packages, private settings, logs or payloads are bundled.
