# Agent guide: github-triage plugin

Category: Development
Folder: plugins/development/github-triage/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Triages a repository's open GitHub issues and pull requests via the gh CLI: optionally merges ready bot and maintainer-approved PRs and spawns review subagents for unreviewed ones, closes already-resolved issues with referenced explanations, cross-links issues with pending fix PRs, and assigns local-only priority and change-size estimates.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| github-triage | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs - incrementally merging passing automated/bot PRs and maintainer-approved ones,... | `skills/github-triage/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | github-triage: A Claude Code skill for triaging the open GitHub issues and pull requests of a | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
