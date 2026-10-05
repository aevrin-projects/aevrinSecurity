# Agent guide: code-understanding

Plugin: code-understanding (Code Auditing)
Skill folder: plugins/code-auditing/code-understanding/skills/code-understanding/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture review on unfamiliar code, and before any vulnerability-hunting pass.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Do not analyze in this context
- What comes back, and how to read it
- The format

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture review on unfamiliar code, and... | First. Always. |
| `resources/ANALYSIS_FORMAT.md` | Analysis Format: The output format for a per-function analysis. The skill body defines what to analyze; this defines how to | When a step points to it, or when you need the detail. |
| `resources/DOMAIN_NOTES.md` | Domain Notes: The format never changes. Whatever the target, you are always asking the same four questions up front - | When a step points to it, or when you need the detail. |
| `resources/FUNCTION_MICRO_ANALYSIS_EXAMPLE.md` | Worked Example: A complete per-function analysis. The subject is C; the format is language-neutral, and the notes at the end | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md on this repository. List the gaps, risks, and weak spots you find. Do not change any code.
- Report: Use plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md on this repository. Write a detailed report to ./reports/code-understanding.md with ratings, evidence, and recommended changes.
- Fix: Read ./reports/code-understanding.md. Apply the recommended changes one at a time, then check each one.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
