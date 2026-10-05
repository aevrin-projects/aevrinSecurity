# Agent guide: review-walkthrough plugin

Category: Development
Folder: plugins/development/review-walkthrough/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| review-walkthrough | Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called. | `skills/review-walkthrough/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Review Walkthrough: Generates an interactive HTML walkthrough of committed changes on the current | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
