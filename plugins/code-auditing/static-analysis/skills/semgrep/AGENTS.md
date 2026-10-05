# Agent guide: semgrep

Plugin: static-analysis (Code Auditing)
Skill folder: plugins/code-auditing/static-analysis/skills/semgrep/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and merges the output to SARIF. Supports two scan modes, "run all" for full ruleset coverage and "important only" for security findings at medium-to-high confidence and impact. Uses Semgrep Pro for cross-file taint analysis when it is available. Use when asked to scan code for vulnerabilities, run a security audit with Semgrep, find bugs, or perform static analysis. For the same scan without the approval gate, use the /static-analysis:semgrep-scan workflow.

## Use this skill when

- Security audit of a codebase
- Finding vulnerabilities before code review
- Scanning for known bug patterns
- First-pass static analysis

## Do not use this skill when

- Binary analysis → Use binary analysis tools
- Already have Semgrep CI configured → Use existing pipeline
- Need cross-file analysis but no Pro license → Consider CodeQL as alternative
- Creating custom Semgrep rules → Use `semgrep-rule-creator` skill
- Porting existing rules to other languages → Use `semgrep-rule-variant-creator` skill

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Essential Principles
- When to Use
- When NOT to Use
- Output Directory
- Prerequisites
- Scan Modes
- Orchestration Architecture
- Running it as a Workflow
- Workflow
- Workflow and agents
- Rationalizations to Reject
- Reference Index
- Success Criteria

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and... | First. Always. |
| `references/rulesets.md` | Semgrep Rulesets Reference: Follow this algorithm to select rulesets based on detected languages and frameworks. | When a step points to it, or when you need the detail. |
| `references/scan-modes.md` | Scan Modes Reference: Full scan with all rulesets and severity levels. Current default behavior. No filtering applied - all findings are reported and triaged. | When a step points to it, or when you need the detail. |
| `workflows/scan-workflow.md` | Semgrep Scan Workflow: Complete 5-step scan execution process. Read from start to finish and follow each step in order. | At the phase it belongs to. |

## Example requests

- Find: Use plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md. Scan this repository. Write a detailed report to ./reports/semgrep.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/semgrep.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
