# Agent guide: semgrep-rule-creator

Plugin: semgrep-rule-creator (Code Auditing)
Skill folder: plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

## Use this skill when

- Writing Semgrep rules for specific bug patterns
- Writing rules to detect security vulnerabilities in your codebase
- Writing taint mode rules for data flow vulnerabilities
- Writing rules to enforce coding standards

## Do not use this skill when

- Running existing Semgrep rulesets
- General static analysis without custom rules (use `static-analysis` skill)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Rationalizations to Reject
- Anti-Patterns
- Strictness Level
- Overview
- Quick Start
- Quick Reference
- Workflow
- Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. | First. Always. |
| `references/quick-reference.md` | Semgrep Rule Quick Reference: Constrain metavariables to specific types (reduces false positives): | When a step points to it, or when you need the detail. |
| `references/workflow.md` | Semgrep Rule Creation Workflow: Detailed workflow for creating production-quality Semgrep rules. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md on this repository. Write the result and the evidence to ./reports/semgrep-rule-creator.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
