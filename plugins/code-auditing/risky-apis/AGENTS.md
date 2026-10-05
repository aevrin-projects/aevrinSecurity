# Agent guide: risky-apis plugin

Category: Code Auditing
Folder: plugins/code-auditing/risky-apis/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Identify error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| risky-apis | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics,... | `skills/risky-apis/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/risky-apis-analyzer.md` | Evaluates APIs, configurations, and library interfaces for misuse resistance and footgun potential. Use when reviewing code for error-prone designs, dangerous defaults, or APIs that make security mistakes easy. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/risky-apis/agents/risky-apis-analyzer.md." |
| `README.md` | Sharp Edges: Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes through developer confusion, laziness, or malice. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
