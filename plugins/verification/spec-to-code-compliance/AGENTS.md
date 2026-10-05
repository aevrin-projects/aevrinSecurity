# Agent guide: spec-to-code-compliance plugin

Category: Verification
Folder: plugins/verification/spec-to-code-compliance/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Check code against the documentation that specifies it: one agent per requirement, divergences refuted before they are reported, evidence cited to the line

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| spec-to-code-compliance | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. Use when comparing... | `skills/spec-to-code-compliance/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/spec-compliance-checker.md` | Checks one documented requirement against the code that should implement it, and returns a verdict with the lines that evidence it. Writes its analysis to disk and returns a compact record. Use for a single requirement; use... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/spec-to-code-compliance/agents/spec-compliance-checker.md." |
| `README.md` | Spec-to-Code Compliance: Check code against the documentation that specifies it. Every gap is either a bug or a documentation fix, and | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
