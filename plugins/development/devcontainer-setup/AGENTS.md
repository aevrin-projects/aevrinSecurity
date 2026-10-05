# Agent guide: devcontainer-setup plugin

Category: Development
Folder: plugins/development/devcontainer-setup/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Create pre-configured devcontainers with Claude Code and language-specific tooling

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| devcontainer-setup | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development... | `skills/devcontainer-setup/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Devcontainer Setup Plugin: Create pre-configured devcontainers with Claude Code and language-specific tooling. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
