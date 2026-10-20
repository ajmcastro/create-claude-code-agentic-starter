# missionlog — project instructions

A Python CLI that reads flight telemetry CSVs and prints a flight summary. Small on purpose: this repo is a reference for agentic workflows with Claude Code.

## Commands

- Install: `pip install -e ".[dev]"`
- Tests: `pytest -q`
- Lint/format: `ruff check . && ruff format .`
- Run: `python -m missionlog data/sample_flight.csv`

## Layout

- `src/missionlog/telemetry.py` — CSV parsing into `Sample` records. No metric logic here.
- `src/missionlog/metrics.py` — pure functions `list[Sample] -> value`. One function per metric.
- `src/missionlog/cli.py` — argument parsing and output only.
- `tests/` — one test module per source module.

## Conventions

- Type hints on every public function. Standard library only in `src/` unless an ADR says otherwise.
- Metrics are pure functions registered in `METRICS` in `metrics.py`. Use the `add-metric` skill to add one.
- Every behaviour change ships with a test. Run `pytest -q` before saying a task is done.
- Significant design choices get an ADR in `docs/adr/` (use the `write-adr` skill).

## Working agreements

- For anything touching more than one module, start in plan mode and get the plan approved.
- Delegate reviews to the `code-reviewer` subagent and test runs to the `test-runner` subagent so their output stays out of the main context.
- Never force-push, never edit `data/` files, never commit secrets. (Hooks enforce part of this; the rest is on you.)
- At the end of a substantial session, run `/session-handoff` to update project memory.

## Project memory

Durable knowledge lives in `docs/memory/`, organised as an index of "rooms". The index is loaded below; open a room's file only when the task touches it.

@docs/memory/INDEX.md
