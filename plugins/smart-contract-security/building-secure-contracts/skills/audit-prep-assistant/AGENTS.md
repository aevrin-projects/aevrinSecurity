# Agent guide: audit-prep-assistant

Plugin: building-secure-contracts (Smart Contract Security)
Skill folder: plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Prepares codebases for security review using Aevrin Security's checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments). Use when preparing your own codebase to be audited by someone else, getting a repository review-ready before an external security review, deciding what to fix before auditors start, or asking what assessors need from a project. For understanding unfamiliar code you are about to audit, use code-understanding instead.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Purpose
- The Preparation Process
- How I Work
- Rationalizations (Do Not Skip)
- Example Output
- REVIEW GOALS DOCUMENT
- STATIC ANALYSIS REPORT
- TEST COVERAGE REPORT
- CODE SCOPE
- BUILD INSTRUCTIONS
- DOCUMENTATION
- DEPLOYMENT INFO
- What You'll Get
- Timeline
- Ready to Prep

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Prepares codebases for security review using Aevrin Security's checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation... | First. Always. |

## Example requests

- Find: Use plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.
- Report: Use plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/audit-prep-assistant.md with ratings, evidence, and recommended changes.
- Fix: Read ./reports/audit-prep-assistant.md. Apply the recommended changes one at a time, then check each one.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
