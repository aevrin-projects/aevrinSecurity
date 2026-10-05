# Agent guide: modern-python plugin

Category: Development
Folder: plugins/development/modern-python/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Modern Python best practices. Use when creating new Python projects, and writing Python scripts, or migrating existing projects from legacy tools.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| modern-python | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. | `skills/modern-python/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Modern Python: Modern Python tooling and best practices using uv, ruff, ty, and pytest. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
