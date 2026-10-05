# Agent guide: second-opinion

Plugin: second-opinion (Development)
Skill folder: plugins/development/second-opinion/skills/second-opinion/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second opinion on code, a codex review, a gemini review, an antigravity review, or /second-opinion.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Review choices
- Input preparation
- Provider references
- Results and failures
- Examples

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second opinion on code, a codex review, a gemini review, an... | First. Always. |
| `references/antigravity-invocation.md` | Antigravity Invocation: Use agy print mode with the prepared prompt as one quoted argument. | When a step points to it, or when you need the detail. |
| `references/codex-invocation.md` | Codex Invocation: Use codex exec with the prepared prompt on stdin. It supports a | When a step points to it, or when you need the detail. |
| `references/gemini-invocation.md` | Gemini CLI Invocation: Retain this path for an explicit Gemini CLI request or an account using | When a step points to it, or when you need the detail. |
| `references/review-input.md` | Review Input: Use one captured patch and the same review instructions across providers. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/second-opinion/skills/second-opinion/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
