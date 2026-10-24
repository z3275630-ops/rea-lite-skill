# Detailed target routing

| Target / question | First tool |
|---|---|
| Native binary, archive, APK/IPA/MSIX/AppX/DMG/pkg | `open_binary` |
| Metadata and inventory after opening | `binary_overview` (provider permitting) |
| Android manifest, code, classes, methods, xrefs | `inspect_android_package` |
| Android resources / manifest decode | `decode_android_resources` |
| One Android class / method | `inspect_android_class`, `inspect_android_method` |
| Android class search / references | `search_android_classes`, `trace_android_references` |
| Managed .NET PE/CLI | `inspect_managed_artifact` |
| Managed member inventory / diff | `inspect_managed_members`, `compare_managed_members` |
| ASAR / extracted JS / Electron app | `analyze_javascript_application` |
| Web page bundle | `analyze_web_bundle` |
| Trace a feature through JS | `trace_application_feature`, `trace_feature` |
| Browser target already open | `list_browser_targets` |
| Browser actions (click, type, navigate) | `capture_browser_scenario` |
| Electron runtime | `list_electron_targets`; check `inspect_electron_fuses` before `--inspect` |
| Electron page / scenario | `inspect_electron_page`, `capture_electron_scenario` |
| HAR / SAZ / qlog capture | `inspect_web_network_capture` |
| Packet field discovery | `inspect_packet_fields` |
| Selected packet fields from PCAP | `inspect_packet_capture` |
| Address/DNS/SNI/protocol summary | `inspect_pcap_capture` |
| Signal decoder discovery / decode | `inspect_signal_decoders`, `decode_signal_recording` |
| Firmware regions / extraction | `inspect_firmware_regions`, `extract_firmware` |
| WASM artifact / interface diff | `inspect_wasm_artifact`, `compare_wasm_interfaces` |
| EVM bytecode interface | `inspect_evm_interface` |
| Go build metadata | `inspect_go_binary` |
| Rust cargo-auditable metadata | `inspect_rust_binary` |
| SQLite snapshot | `inspect_sqlite_database` (schema first, then rows) |
| Offline ELF layout | `inspect_binary_layout` |
| Recorded crash / core | `inspect_recorded_crash` |
| PE resources | `inspect_pe_resources` |
| Mach-O / plist / signature / dylib | `inspect_macho`, `inspect_plist`, `inspect_signature`, `trace_dylib_resolution` |
| Dart AOT / Flutter build | `inspect_dart_aot`, `identify_flutter_build` |
| HarmonyOS HAP/HSP/App Pack | `project_harmony_application_graph` |
| IDA provider | `open_binary` with `provider_id: "ida"` |
| JEB project / units / item | `open_jeb_project`, `list_jeb_units`, `decompile_jeb_item` |
| Frida session | `start_frida_session`, `load_frida_script`, `resume_frida_session`, `close_frida_session` |
| GDB / Rizin / Cutter debug | `start_gdb_session`, `start_rizin_debug_session`, `cutter_command` |
| Process capture / diff | `capture_process_scenario`, `compare_process_captures` |
| Version / function / artifact diff | `compare_application_versions`, `compare_functions`, `compare_artifacts`, `find_changed_behavior` |
| Source vs bundle | `compare_source_to_bundle` |
| Static vs runtime reconciliation | `correlate_static_and_runtime`, `reconcile_javascript_runtime` |


Read only the guide matching the selected route:

- [Native / managed / packages](native-and-artifacts.md)
- [Android](android-applications.md)
- [JavaScript](javascript-applications.md)
- [Runtime](runtime-observation.md)
- [Evidence and comparisons](evidence-workflows.md)
- [Provider constraints](provider-notes.md)
- [All 207 tool names](tool-index.md)
