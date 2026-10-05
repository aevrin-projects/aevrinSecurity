# Agent guide: sarif-parsing

Plugin: static-analysis (Code Auditing)
Skill folder: plugins/code-auditing/static-analysis/skills/sarif-parsing/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans - use the Semgrep or CodeQL skills for that.

## Use this skill when

- Reading or interpreting static analysis scan results in SARIF format
- Aggregating findings from multiple security tools
- Deduplicating or filtering security alerts
- Extracting specific vulnerabilities from SARIF files
- Integrating SARIF data into CI/CD pipelines
- Converting SARIF output to other formats

## Do not use this skill when

- Running static analysis scans (use CodeQL or Semgrep skills instead)
- Writing CodeQL or Semgrep rules (use their respective skills)
- Analyzing source code directly (SARIF is for processing existing scan results)
- Triaging findings without SARIF input (use similar-bug-finder or audit skills)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- SARIF Structure Overview
- Tool Selection Guide
- Strategy 1: Quick Analysis with jq
- Strategy 2: Python with pysarif
- Strategy 3: Python with sarif-tools
- Strategy 4: Aggregating Multiple SARIF Files
- Strategy 5: Extracting Actionable Data
- Common Pitfalls and Solutions
- CI/CD Integration Patterns
- Key Principles
- Skill Resources
- Reference Links

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output".... | First. Always. |
| `resources/jq-queries.md` | SARIF jq Query Reference: Ready-to-use jq queries for common SARIF parsing tasks. | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md. Scan this repository. Write a detailed report to ./reports/sarif-parsing.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/sarif-parsing.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
