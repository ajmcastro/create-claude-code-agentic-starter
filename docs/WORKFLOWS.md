# Workflows

How to drive this repo with Claude Code. Each workflow names the building blocks it exercises.

## 1. Explore → plan → build → verify (default for multi-file changes)

1. **Explore.** Ask a question about the code, e.g. "How does a CSV row become a metric value?" Claude delegates broad searches to the built-in Explore subagent, keeping the main context small.
2. **Plan.** Switch to plan mode (`Shift+Tab` cycles permission modes; plan mode is read-only). Ask for the change. Claude researches and presents a plan; nothing is edited until you approve.
3. **Build.** Approve the plan. The `lint-on-edit` hook formats each Python file as it is written and feeds lint errors back to Claude.
4. **Verify.** Ask Claude to use the `test-runner` subagent, then the `code-reviewer` subagent. Only summaries return to the main conversation.
5. **Remember.** Run `/session-handoff` to file durable learnings in `docs/memory/`.

## 2. Add a metric (skill-driven)

Say "add a metric for total climb in metres". The `add-metric` skill's description matches, so Claude loads it and follows its checklist: definition → test first → implementation → registry → verification.

## 3. Record a decision

`/write-adr should telemetry parsing accept JSON as well as CSV?` — produces a `Proposed` ADR from the template and links it from the decisions room.

## 4. See the guardrails work

- Ask Claude to `git push --force` → blocked by `guard-bash`, with the reason returned to Claude.
- Ask Claude to edit `data/sample_flight.csv` → denied by the `permissions.deny` rules in `.claude/settings.json`.

## Where each concept lives

| Concept | Advisory or enforced | Location |
|---|---|---|
| Conventions | Advisory | `CLAUDE.md` |
| Memory palace | Advisory | `docs/memory/` |
| Procedures | Advisory | `.claude/skills/` |
| Specialist workers | Tool limits enforced | `.claude/agents/` |
| Guardrails | Enforced | `.claude/settings.json`, `.claude/hooks/` |
