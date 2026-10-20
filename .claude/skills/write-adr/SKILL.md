---
name: write-adr
description: Write an architecture decision record (ADR) in docs/adr using the project template. Use when a significant design choice is being made or questioned, or when the user asks for an ADR.
---

# Write an ADR

The decision or question to record: $ARGUMENTS

1. List `docs/adr/` and pick the next number (zero-padded to 4 digits).
2. Copy the structure from [template.md](template.md). Keep every heading.
3. Fill it in:
   - **Context:** the forces at play, in facts. Read the relevant code before writing this.
   - **Options:** at least two, each with honest pros and cons.
   - **Decision:** if the user has not decided, set status to `Proposed` and write "Pending" — do not decide for them.
   - **Consequences:** what becomes easier, what becomes harder, what we must now watch.
4. Save as `docs/adr/NNNN-short-kebab-title.md`.
5. Add a one-line pointer to the ADR in `docs/memory/rooms/decisions.md`.

Keep it under one page. ADRs are read later by people (and agents) without your context, so prefer concrete statements over adjectives.
