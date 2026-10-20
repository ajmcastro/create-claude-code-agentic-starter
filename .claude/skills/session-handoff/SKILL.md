---
name: session-handoff
description: Save durable learnings from the current session into the project memory in docs/memory. Use at the end of a substantial session or when the user says to save, remember or hand off what was learned.
disable-model-invocation: true
---

# Session handoff

Project memory is organised like a memory palace: `docs/memory/INDEX.md` is the entrance hall (always loaded through `CLAUDE.md`), and each file in `docs/memory/rooms/` is a room loaded only when relevant.

1. **Collect candidates.** Review this session and list facts that will still be true and useful in a month: decisions, conventions, gotchas, domain facts, open questions the user stated.
2. **Filter hard.** Drop anything that is:
   - already in a room or in `CLAUDE.md`
   - re-derivable from the code or git history
   - the moving state of a task that will finish soon
   - a guess you made that the user did not confirm
3. **File each fact in exactly one room.** Read the room first, then add or update one bullet. Rooms:
   - `rooms/architecture.md` — module boundaries, data flow
   - `rooms/domain.md` — telemetry and flight-domain facts
   - `rooms/decisions.md` — one-line pointers to ADRs and small decisions
   - `rooms/gotchas.md` — things that broke or surprised us
   If a fact fits none, create a new room and add it to the index.
4. **Update the index** only if a room was added or its one-line summary is now wrong. Keep `INDEX.md` under 40 lines — it is loaded every session.
5. **Report** to the user in at most five bullets what was saved and where.

Never store secrets, credentials or personal data in memory files; they are committed to git.
