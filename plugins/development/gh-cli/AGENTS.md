# Agent guide: gh-cli plugin

Category: Development
Folder: plugins/development/gh-cli/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Intercepts GitHub URL fetches (WebFetch and MCP fetch tools) and curl/wget commands, redirecting to the authenticated gh CLI.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| gh-cli | Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues. | `skills/gh-cli/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | gh-cli: A Claude Code plugin that intercepts GitHub URL fetches and redirects Claude to use the authenticated gh CLI instead. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
