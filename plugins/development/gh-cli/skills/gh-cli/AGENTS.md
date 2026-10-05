# Agent guide: gh-cli

Plugin: gh-cli (Development)
Skill folder: plugins/development/gh-cli/skills/gh-cli/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

## Use this skill when

- Working with GitHub repositories, pull requests, issues, releases, or raw file URLs.
- You need authenticated access to private repositories or higher API rate limits.
- You are about to use `curl`, `wget`, `WebFetch`, or an MCP fetch tool against GitHub.

## Do not use this skill when

- The target is not GitHub.
- Plain local git operations already solve the task.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Guidance

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues. | First. Always. |

## Example requests

- Use: Use plugins/development/gh-cli/skills/gh-cli/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
