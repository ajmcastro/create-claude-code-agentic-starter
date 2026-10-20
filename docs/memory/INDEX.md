# Project memory — index

The entrance hall of the project's memory palace. This file is loaded into every session via `CLAUDE.md`; keep it short. Each room holds detail and is opened only when a task touches it.

| Room | Open it when… |
|---|---|
| [architecture](rooms/architecture.md) | changing module boundaries or data flow |
| [domain](rooms/domain.md) | working with telemetry fields, units or flight phases |
| [decisions](rooms/decisions.md) | revisiting a design choice; pointers to ADRs |
| [gotchas](rooms/gotchas.md) | something behaves unexpectedly |

## Always true

- Metrics are pure functions over `list[Sample]`; parsing lives only in `telemetry.py`.
- Units are SI throughout (m, s, m/s).
