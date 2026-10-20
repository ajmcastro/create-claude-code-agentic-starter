# Room: architecture

- Data flow: CSV → `telemetry.load_samples()` → `list[Sample]` → each function in `metrics.METRICS` → `cli` prints a table.
- `Sample` is a frozen dataclass; nothing mutates samples after parsing.
- The CLI has no logic beyond formatting, so every metric is testable without I/O.
