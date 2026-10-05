# Agent guide: pr-improver

Plugin: code-improver (Development)
Skill folder: plugins/development/code-improver/skills/pr-improver/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the branch touched. Reviews are performed by an installed PR-review skill (default: pr-review-toolkit's review-pr). Use to fix review findings on a branch before opening or updating a pull request ('clean up this branch', 'fix this PR until review passes', 'run review-and-fix on my changes'). NOT for a one-time review - run the PR-review skill directly.

## Do not use this skill when

- **One-time review**: run the PR-review skill directly; the loop's value is iteration
- **A skill**: use the `skill-improver` entry - it wires the right reviewer
- **Unpushed exploratory work**: review-and-fix loops harden a diff; while the shape is

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
- When NOT to use

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the branch touched. Reviews are performed by an installed... | First. Always. |

## Example requests

- Use: Use plugins/development/code-improver/skills/pr-improver/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
