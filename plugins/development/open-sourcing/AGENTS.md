# Agent guide: open-sourcing plugin

Category: Development
Folder: plugins/development/open-sourcing/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Prepares a repository for public open-source release: secrets-history hygiene, license selection, documentation and CI readiness checks, and language-specific packaging and release guidance.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| open-sourcing | This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source readiness", "choose a license... | `skills/open-sourcing/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | open-sourcing: Prepares a repository for public open-source release. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
