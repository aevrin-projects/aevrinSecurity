# Agent guide: differential-review

Plugin: differential-review (Code Auditing)
Skill folder: plugins/code-auditing/differential-review/skills/differential-review/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting callers, checks test coverage of modified code, and generates a markdown report. Use when reviewing a PR, commit, or diff for security vulnerabilities, checking whether a change re-introduces a previously fixed bug, asking what else a change could break, or finding which modified code has no test covering it.

## Do not use this skill when

- **Greenfield code** (no baseline to compare)
- **Documentation-only changes** (no security impact)
- **Formatting/linting** (cosmetic changes)
- **User explicitly requests quick summary only** (they accept risk)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Core Principles
- Rationalizations (Do Not Skip)
- Quick Reference
- Workflow Overview
- Decision Tree
- Agents
- Quality Checklist
- Integration
- Example Usage
- When NOT to Use This Skill
- Red Flags (Stop and Investigate)
- Tips for Best Results
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting callers, checks test coverage of modified code, and... | First. Always. |
| `adversarial.md` | Adversarial Vulnerability Analysis (Phase 5): Structured methodology for finding vulnerabilities through attacker modeling. | When a step points to it. |
| `methodology.md` | Differential Review Methodology: Detailed phase-by-phase workflow for security-focused code review. | When a step points to it. |
| `patterns.md` | Common Vulnerability Patterns: Quick reference for detecting common security issues in code changes. | When a step points to it. |
| `reporting.md` | Report Generation (Phase 6): Comprehensive markdown report structure and formatting guidelines. | When a step points to it. |

## Example requests

- Find: Use plugins/code-auditing/differential-review/skills/differential-review/SKILL.md. Scan the changes between main and my current branch. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/differential-review/skills/differential-review/SKILL.md. Scan the changes between main and my current branch. Write a detailed report to ./reports/differential-review.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/differential-review.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
