# Agent guide: review-walkthrough

Plugin: review-walkthrough (Development)
Skill folder: plugins/development/review-walkthrough/skills/review-walkthrough/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Capture the branch diff
- Shape the review
- Render the artifact

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called. | First. Always. |

## Example requests

- Use: Use plugins/development/review-walkthrough/skills/review-walkthrough/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
