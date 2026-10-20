---
name: add-metric
description: Add a new flight telemetry metric to missionlog end to end (function, registry, test, docs). Use when the user asks to compute, add or report a new statistic about a flight.
---

# Add a telemetry metric

Follow these steps in order. Do not skip the test.

1. **Clarify the definition.** State the metric in one sentence with its unit (e.g. "maximum climb rate in m/s, computed between consecutive samples"). If the definition is ambiguous (units, edge cases, empty input), ask before writing code.
2. **Check the data.** Read `src/missionlog/telemetry.py` to confirm the needed fields exist on `Sample`. If a field is missing, stop and propose the parser change first.
3. **Write the test first** in `tests/test_metrics.py`:
   - one test on a small hand-built list of `Sample`s with a hand-calculated expected value
   - one test for the edge case (fewer than two samples, or empty list)
4. **Implement** a pure function in `src/missionlog/metrics.py`:
   - signature `def <name>(samples: list[Sample]) -> float`
   - docstring with the definition and unit
   - no I/O, no printing
5. **Register** it in the `METRICS` dict in `metrics.py` with a human-readable label including the unit.
6. **Verify:** run `pytest -q`. If it fails, fix and re-run. Then run `python -m missionlog data/sample_flight.csv` and check the new line looks sensible.
7. **Record:** if you made a non-obvious choice (interpolation, filtering, units), add one line to `docs/memory/rooms/domain.md`.

## Gotchas

- Timestamps are in seconds as floats; consecutive samples can share a timestamp. Skip zero-duration intervals instead of dividing by zero.
- Altitude is metres above take-off point, not above sea level.
- Keep metrics independent: never call one metric function from another.
