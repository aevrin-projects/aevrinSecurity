# Agent guide: code-understanding plugin

Category: Code Auditing
Folder: plugins/code-auditing/code-understanding/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Understand a codebase before looking for bugs in it. Reads it function by function, records what each one assumes and depends on, and saves the write-ups to files instead of filling up the conversation.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| code-understanding | Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture... | `skills/code-understanding/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/function-analyzer.md` | Analyzes one function in depth for audit context: invariants, assumptions, and what its callees establish. Writes the prose analysis to disk and returns a compact record. Use for dense functions, data-flow chains,... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/code-understanding/agents/function-analyzer.md." |
| `README.md` | Audit Context Building: Understand a codebase before you go looking for bugs in it. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
