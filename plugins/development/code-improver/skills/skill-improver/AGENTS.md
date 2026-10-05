# Agent guide: skill-improver

Plugin: code-improver (Development)
Skill folder: plugins/development/code-improver/skills/skill-improver/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes stop converging, and a mechanical scope guard. Reviews are performed by the plugin-dev skill-reviewer agent. Use to fix skill quality issues, iteratively refine a skill, or resume a loop after an escalation ('fix my skill', 'improve this skill until it passes review', 'skill improvement loop'). NOT for a one-time review - use the plugin-dev skill-reviewer agent directly.

## Do not use this skill when

- **One-time review**: dispatch the `plugin-dev:skill-reviewer` agent directly
- **Quick single fixes**: edit the file directly
- **Non-skill targets**: use the `code-improver` skill with a reviewer that fits the
- **Exploratory drafting**: manual iteration gives more control while the shape is fluid

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Starting the loop
- Relaying the result
- Continuing after an escalation
- What the loop enforces (so you do not have to)
- When NOT to use

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes stop converging, and a mechanical scope guard. Reviews are... | First. Always. |

## Example requests

- Use: Use plugins/development/code-improver/skills/skill-improver/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
