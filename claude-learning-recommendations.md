# Learning Claude for the Tekever application

Recommendations for building working knowledge of Claude's skills, workflows, plan mode, memory and reusable structures.

Prepared 20 October 2026. Claude Code changes quickly, so check the official docs before relying on any detail here.

---

## 1. Learn the official building blocks

Most of the terms in the job ad are **Claude Code** concepts. Learn each one from the official docs.

| Concept | What it is | Official doc |
|---|---|---|
| **Skills** | Reusable folders of instructions (`SKILL.md` + optional files). Claude loads them when relevant, or you invoke them as `/skill-name`. Only the short description is always in context; the rest loads on demand. | [Skills in Claude Code](https://code.claude.com/docs/en/skills) · [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) · [Skills best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) |
| **Plan mode** | A read-only permission mode: Claude researches and proposes a plan, then waits for approval before editing. | [Permission modes](https://code.claude.com/docs/en/permission-modes) |
| **Subagents** | Specialised agents with their own context window, system prompt, tool restrictions and model. Built-ins include Explore, Plan and general-purpose. | [Create custom subagents](https://code.claude.com/docs/en/sub-agents) |
| **Hooks** | Shell commands that run at fixed lifecycle points (e.g. `PreToolUse`, `PostToolUse`, `SessionStart`). They are deterministic; CLAUDE.md and skills are only advisory. | [Hooks reference](https://code.claude.com/docs/en/hooks) |
| **Memory (CLAUDE.md)** | Project, user and local instruction files loaded at startup, plus Claude's auto-memory and per-subagent memory. | [Memory](https://code.claude.com/docs/en/memory) |
| **Plugins** | A way to package and share skills, subagents, hooks and MCP servers. | [Plugins overview](https://code.claude.com/docs/en/plugins/overview) |
| **MCP** | The protocol for connecting Claude to external tools and data. | [MCP in Claude Code](https://code.claude.com/docs/en/mcp) |

The full index of Claude Code docs pages is at <https://code.claude.com/docs/llms.txt>.

Engineering background: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (Anthropic engineering blog).

**Interview point worth having ready:** hooks enforce, instructions advise. Use a hook for anything that must always happen (formatting, blocking dangerous commands, running tests); use CLAUDE.md or a skill for judgement and conventions.

---

## 2. Take the free Anthropic Academy courses

- Course catalogue: <https://anthropic.skilljar.com/>
- Hub: <https://anthropic.com/learn>

Suggested order for the coding-agent track (from a third-party guide):

1. Claude Code 101
2. Claude Code in Action
3. Introduction to Agent Skills (short: about 6 lessons / 30 minutes, per third-party sources)
4. Introduction to Subagents

Secondary sources disagree on how many courses exist (13, 17 or 21 depending on the date), so check the catalogue directly.

---

## 3. "Memory palace": ask Tekever what they mean

This is **not** an official Anthropic feature as far as I could find. It most likely refers to one of these:

- **MemPalace**, an open-source memory system that organises data as a virtual "palace" (wings per project, person, topic). It can be installed as a Claude Code plugin. Coverage: [36Kr article](https://eu.36kr.com/en/p/3758096887398914).
- **Community "Memory Palace" skills** in third-party registries, e.g. [claudskills.com/skills/memory-palace](https://claudskills.com/skills/memory-palace/). These are not vetted by Anthropic.
- A general pattern of **hierarchical, structured memory files** for an agent.

Recommended action: ask the recruiter or hiring manager which one they mean. Either way, know the native options well (CLAUDE.md, auto-memory, subagent `memory:` scopes), since third-party systems build on top of them.

---

## 4. Build something and put it on GitHub

A starter project accompanies this file (`claude-code-agentic-starter`). It contains:

- a `CLAUDE.md` with imported memory files
- three project skills (a workflow skill, a templated skill, a memory skill)
- two subagents (read-only reviewer with persistent memory, cheap test runner)
- hooks that format/lint after edits and block dangerous shell commands
- a small hierarchical memory layer (a lightweight "memory palace")
- a small Python app with tests for all of the above to act on

Your multi-agent systems background maps directly onto this: orchestrator → subagents with isolated context, tool restrictions as capability boundaries, and memory split into procedural (skills), declarative (CLAUDE.md / memory files) and episodic (session logs). Explaining those trade-offs will likely matter more than knowing commands.

---

## 5. Caveats

- Claude Code changes quickly; the official docs at code.claude.com and platform.claude.com are the authority, not blog posts.
- Some sources above are third-party summaries (marked as such).
- I don't have verified information about Tekever's internal setup or how they use Claude.

## Sources

- [Agent Skills overview (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skills in Claude Code (Anthropic)](https://code.claude.com/docs/en/skills)
- [Create custom subagents (Anthropic)](https://code.claude.com/docs/en/sub-agents)
- [Hooks reference (Anthropic)](https://code.claude.com/docs/en/hooks)
- [Anthropic Academy course guide (third-party, Tutorials Dojo)](https://tutorialsdojo.com/?p=40340)
- [Anthropic Academy overview (third-party)](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)
- [MemPalace coverage (36Kr)](https://eu.36kr.com/en/p/3758096887398914)
- [Claude Code 9-step loop (third-party)](https://mer.vin/2026/07/claude-code-9-step-loop-explore-plan-hooks-and-senior-style-review/)
