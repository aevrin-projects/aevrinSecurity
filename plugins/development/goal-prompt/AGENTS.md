# Agent guide: goal-prompt plugin

Category: Development
Folder: plugins/development/goal-prompt/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Drafts copy-ready /goal commands for goal mode in Claude Code and Codex: verifiable completion conditions with stop bounds, normalized to a single line under the 4,000-character cap.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| goal-prompt | Drafts copy-paste-ready /goal commands for goal mode in Claude Code and Codex. Use when the user asks to create, write, rewrite, improve, compress, clean up, or prepare a goal prompt, goal... | `skills/goal-prompt/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | goal-prompt: Turns a task description into a copy-paste-ready /goal command for goal mode in Claude Code or Codex. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
