# Agent guide: second-opinion plugin

Category: Development
Folder: plugins/development/second-opinion/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| second-opinion | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second opinion on code, a codex review,... | `skills/second-opinion/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | second-opinion: Get an independent review of uncommitted changes, a branch diff, or a | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
