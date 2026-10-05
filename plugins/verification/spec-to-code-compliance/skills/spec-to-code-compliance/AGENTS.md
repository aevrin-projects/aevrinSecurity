# Agent guide: spec-to-code-compliance

Plugin: spec-to-code-compliance (Verification)
Skill folder: plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. Use when comparing an implementation against a whitepaper, protocol spec, or design document.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Do not check requirements in this context
- What comes back, and how to read it
- Judgment the workflow does not make for you
- The target does not have to be a contract
- Reference

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. Use when comparing an implementation against a... | First. Always. |
| `resources/ANALYSIS_FORMAT.md` | Analysis Format: The output format for a per-requirement analysis. The agent defines what to check; this defines how to write it | When a step points to it, or when you need the detail. |
| `resources/DIVERGENCE_RUBRIC.md` | Divergence Rubric: Severity is about consequence, not about how far the code strayed from the words. A requirement the code | When a step points to it, or when you need the detail. |
| `resources/DOMAIN_NOTES.md` | Domain Notes: The question never changes. For each requirement: what does it demand of an implementation, where would that be | When a step points to it, or when you need the detail. |
| `resources/WORKED_EXAMPLE.md` | Worked Examples: Three requirements against real code shapes, one per verdict that is easy to get wrong. Read these for | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md. Scan this repository and its specification. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md. Scan this repository and its specification. Write a detailed report to ./reports/spec-to-code-compliance.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/spec-to-code-compliance.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
