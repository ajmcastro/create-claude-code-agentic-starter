# 0001. Standard library only in src/

- **Status:** Accepted
- **Date:** 2026-10-20

## Context

missionlog parses small CSV files (thousands of rows) and computes a handful of scalar metrics. It is also a reference project, so it should install instantly and be easy to read.

## Options

### Option A — standard library (`csv`, `dataclasses`)

- Pros: zero dependencies, fast install, every line is readable without library knowledge.
- Cons: manual parsing and type conversion; vectorised maths not available.

### Option B — pandas

- Pros: concise column operations, built-in resampling.
- Cons: heavy dependency for tiny inputs; hides logic that the tests are meant to make explicit.

## Decision

Option A. Input sizes are small and readability of each metric matters more than brevity.

## Consequences

- Easier: installing, reviewing, testing each metric in isolation.
- Harder: time-series operations such as resampling would need hand-written code.
- To watch: if inputs grow past ~1M rows or we need resampling, revisit with a new ADR.
