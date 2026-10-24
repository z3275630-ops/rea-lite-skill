# Provider notes (REA 6.7.0)

**IDA.** `open_binary` with `provider_id: "ida"`, passing the original input binary — not `.idb`/`.i64`. The legacy attached profile binds the already-open GUI input by SHA-256 and leaves the database open; the modern headless profile creates and closes a private database. IDA does not supply `binary_overview`. Live IDA results are not replayed from snapshots.

**Ghidra.** Needs `GHIDRA_INSTALL_DIR` and `JAVA_HOME`. Raw input support depends on the host: Windows Ghidra P0 admits only raw `6502`; the POSIX lane has additional architecture/entry profiles. Supports Windows ARM PE (ARMNT/Thumb-2, ARM64) on the x64 host lane, and big-endian m68k raw images. ARM64EC/ARM64X and Windows-on-Arm hosts are unverified.

**JADX.** APK load and operation deadlines can be extended with `REA_JADX_OPERATION_TIMEOUT_MS`; `doctor` reports the effective value. Multiple locale tables are supported through repeatable `locales`.

**JEB.** REA exposes four compatibility tools through `server: "rea"`. The default engine endpoint is `http://127.0.0.1:8425/mcp`; `REA_JEB_MCP_URL` can select another validated literal-loopback endpoint. Start your existing JEB MCP service using the JEB GUI or its documented programmatic launcher; REA never launches JEB. A separately configured `server: "jeb"` is optional: discover its actual tools, parameter casing and project capabilities instead of assuming a fixed catalog. Some headless clients do not advertise project opening; inspect the existing client and units before requesting it. Preserve the operator's current project.

**Kuna.** Requires `REA_KUNA_COMMAND`; the adapter accepts Linux and macOS hosts and is verified with Kuna 1.833. Windows, PE, and universal Mach-O are unsupported. Answers procedure lists, lookups, pseudocode, assembly, and `analyze_function` from a cached whole-program export. Callers/callees use a body-free graph; `xrefs` returns exact-address incoming sites and filters forwarding aliases. Typed references, CFG, raw-memory tools, and annotations are unsupported. Indirect targets can make relationship coverage partial.

**Firmware.** `inspect_firmware_regions` / `extract_firmware` use caller-supplied Binwalk/Unblob on Linux. `extract_firmware` needs a new absolute output directory. Do not claim support on a host without those tools.

**PCAP / signal.** `inspect_packet_capture` requires Linux with util-linux `prlimit` and `REA_TSHARK_COMMAND`. `inspect_pcap_capture` requires Wireshark 4.x tshark/capinfos, with Linux prlimit or Windows Job Objects. Signal decoding needs sigrok-cli 0.7.2 through `REA_SIGROK_COMMAND` on Linux with prlimit. These read recordings; they do not acquire traffic or hardware signals.

**Browser / Electron.** Use `list_browser_targets` for an already-open page and `capture_browser_scenario` for declared actions only. Before an Electron main-process Inspector attempt, check `inspect_electron_fuses`; if `EnableNodeCliInspectArguments` is disabled, the app ignores `--inspect`.

**Android / ADB.** Device serial must match `adb devices` exactly. Split APK sets are pulled as base plus every split. `pull_adb_package` creates a package-named subdirectory that must not already exist. Do not infer app behavior from package names alone.

**Frida / GDB / Rizin.** Runtime sessions are owned and cancellable; close them explicitly. For GDB, provide an inferior TTY so a live target can be safely detached.


For domain details, read the matching upstream guide linked from [routing.md](routing.md).
