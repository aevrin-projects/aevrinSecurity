# Agent guide: similar-bug-finder plugin

Category: Code Auditing
Folder: plugins/code-auditing/similar-bug-finder/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Find similar vulnerabilities and bugs across codebases using pattern-based analysis

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| similar-bug-finder | Hunts for the other instances of a bug already found - the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or bad pattern turns up in a specific... | `skills/similar-bug-finder/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Variant Analysis: Find similar vulnerabilities and bugs across codebases using pattern-based analysis. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
