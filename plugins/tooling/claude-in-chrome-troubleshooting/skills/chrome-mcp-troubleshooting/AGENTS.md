# Agent guide: chrome-mcp-troubleshooting

Plugin: claude-in-chrome-troubleshooting (Tooling)
Skill folder: plugins/tooling/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

## Use this skill when

- `mcp__claude-in-chrome__*` tools fail with "Browser extension is not connected"
- Browser automation works erratically or times out
- After updating Claude Code or Claude.app
- When switching between Claude Code CLI and Claude.app (Cowork)
- Native host process is running but MCP tools still fail

## Do not use this skill when

- **Linux or Windows users** - This skill covers macOS-specific paths and tools (`~/Library/Application Support/`, `osascript`)
- General Chrome automation issues unrelated to the Claude extension
- Claude.app desktop issues (not browser-related)
- Network connectivity problems
- Chrome extension installation issues (use Chrome Web Store support)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- The Claude.app vs Claude Code Conflict (Primary Issue)
- Quick Diagnosis
- Critical Insight
- Full Reset Procedure (Claude Code CLI)
- Other Common Causes
- Diagnostic Deep Dive
- File Reference
- Summary

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically. | First. Always. |

## Example requests

- Use: Use plugins/tooling/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
