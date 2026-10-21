# claude-code-agentic-starter

A small, working reference project that shows how to structure a repository for **agentic development with Claude Code**: skills, subagents, hooks, plan-mode workflows and a hierarchical project memory.

The application itself is deliberately small — `missionlog`, a Python CLI that summarises flight telemetry from CSV files — so that the interesting part is the **agent configuration around it**, not the app.

> Status: learning / portfolio project. Claude Code evolves quickly; every config format here was checked against the official docs in October 2026. If something stops working, check the linked docs first.

---

## What's inside

```
.
├── CLAUDE.md                     # Project instructions + imports of the memory index
├── .claude/
│   ├── settings.json             # Permissions + hooks (deterministic guardrails)
│   ├── hooks/
│   │   ├── guard-bash.py         # PreToolUse: blocks destructive shell commands
│   │   └── lint-on-edit.py       # PostToolUse: ruff format + check after every edit
│   ├── skills/
│   │   ├── add-metric/           # Workflow skill: add a new telemetry metric end-to-end
│   │   ├── write-adr/            # Templated skill: architecture decision records
│   │   └── session-handoff/      # Memory skill: write what was learned to docs/memory
│   └── agents/
│       ├── code-reviewer.md      # Read-only reviewer with persistent project memory
│       └── test-runner.md        # Cheap model, runs tests, returns only failures
├── docs/
│   ├── memory/                   # Lightweight "memory palace": index → rooms → notes
│   ├── adr/                      # Architecture decision records
│   └── WORKFLOWS.md              # How to drive the repo: explore → plan → build → verify
├── src/missionlog/               # The sample app
├── tests/                        # pytest suite
└── data/sample_flight.csv        # Sample telemetry
```

## The building blocks, and why each is here

| Piece | File(s) | Role | Deterministic? |
|---|---|---|---|
| Project instructions | `CLAUDE.md` | Conventions, commands, boundaries | No — advisory |
| Hierarchical memory | `docs/memory/` (imported from `CLAUDE.md`) | Durable project knowledge, organised by "room" | No — advisory |
| Skills | `.claude/skills/*/SKILL.md` | Reusable procedures, loaded on demand | No — advisory |
| Subagents | `.claude/agents/*.md` | Isolated context, restricted tools, chosen model | Tool limits are enforced |
| Hooks | `.claude/settings.json` + `.claude/hooks/` | Always-on guardrails | **Yes** |
| Plan mode | `docs/WORKFLOWS.md` | Read-only research before edits | Enforced by permission mode |

**Design principle:** anything that *must* happen is a hook; anything that needs *judgement* is a skill or instruction. This is the same split as hard constraints vs. policies in a multi-agent system.

### Mapping to multi-agent systems concepts

| MAS concept | Claude Code equivalent here |
|---|---|
| Orchestrator / coordinator | Main Claude Code session |
| Specialised agents with bounded capabilities | `code-reviewer` (read-only), `test-runner` (Bash + Read only) |
| Capability / action-space restriction | Subagent `tools:` allowlist; `permissions.deny` |
| Procedural knowledge | Skills |
| Declarative / shared knowledge base | `CLAUDE.md` + `docs/memory/` |
| Agent-local learned knowledge | `memory: project` on `code-reviewer` |
| Norms / institutions enforced by the environment | Hooks |

---

## Getting started

Requirements: [uv](https://docs.astral.sh/uv/), [Claude Code](https://code.claude.com/docs/en/overview), and `make`. The setup command installs Python 3.11 and the project environment; you do not need to install Python separately.

If uv is not installed yet, install it using the instructions for your platform:

**macOS and Linux**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

See the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/) for other installation options. After installing uv, open a new terminal and continue:

```bash
git clone https://github.com/<you>/claude-code-agentic-starter.git
cd claude-code-agentic-starter
make setup
make test
make run
```

`make setup` installs Python 3.11 with uv, pins it for this project in `.python-version`, and syncs the project and development dependencies into `.venv`. Run `make help` to see available commands. You can also pass a different CSV to the CLI with `make run ARGS="path/to/flight.csv"`.

Activate the environment before starting Claude Code so its lint-on-edit hook can find the project-installed Ruff:

```bash
source .venv/bin/activate
claude
```

Accept the workspace trust prompt — project hooks only run in trusted folders.

## Things to try (and to demo in an interview)

1. **Skill, auto-invoked:** "Add a metric for maximum climb rate." Claude should pick up the `add-metric` skill and follow its checklist.
2. **Skill, invoked explicitly:** `/write-adr use pandas instead of the csv module?`
3. **Plan mode:** press `Shift+Tab` until plan mode is active, then ask for a refactor. Claude researches and proposes without editing.
4. **Subagent delegation:** "Use the code-reviewer subagent to review my last change." Then check `.claude/agent-memory/code-reviewer/` — it accumulates review notes across sessions.
5. **Hook enforcement:** ask Claude to run `git push --force`. The `guard-bash` hook blocks it, and Claude sees the reason.
6. **Memory:** at the end of a session, run `/session-handoff`. It writes durable learnings into the right "room" in `docs/memory/`, which the next session loads through `CLAUDE.md`.

## Official documentation

- Skills: <https://code.claude.com/docs/en/skills>
- Subagents: <https://code.claude.com/docs/en/sub-agents>
- Hooks: <https://code.claude.com/docs/en/hooks>
- Memory / CLAUDE.md: <https://code.claude.com/docs/en/memory>
- Permission modes (incl. plan mode): <https://code.claude.com/docs/en/permission-modes>
- Plugins (for packaging this later): <https://code.claude.com/docs/en/plugins/overview>

## Ideas for extending it

- Package `.claude/` as a **plugin** so others can install the skills and agents in one step.
- Add an **MCP server** (e.g. a read-only telemetry store) scoped to a subagent via `mcpServers:`.
- Add a `SessionStart` hook that prints the current memory index, and compare it with the `@import` approach.
- Write evals for the skills: a set of prompts and the behaviour you expect.

## License

MIT
