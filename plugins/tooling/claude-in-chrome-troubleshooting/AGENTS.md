# Agent guide: claude-in-chrome-troubleshooting plugin

Category: Tooling
Folder: plugins/tooling/claude-in-chrome-troubleshooting/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Diagnose and fix Claude in Chrome MCP extension connectivity issues

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| chrome-mcp-troubleshooting | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically. | `skills/chrome-mcp-troubleshooting/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Claude in Chrome Troubleshooting: Diagnose and fix Claude in Chrome MCP extension connectivity issues. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
