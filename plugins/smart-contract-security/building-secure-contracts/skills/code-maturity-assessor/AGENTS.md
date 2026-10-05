# Agent guide: code-maturity-assessor

Plugin: building-secure-contracts (Smart Contract Security)
Skill folder: plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Systematic code maturity assessment using Aevrin Security's 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing, then produces a scorecard with evidence-based ratings and a priority-ordered roadmap. Use when assessing or scoring the maturity of a smart contract or blockchain codebase, producing a maturity scorecard or evaluation, or judging how mature, well-tested, or well-documented such a project is against a rubric.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Purpose
- How This Works
- Rating System
- The 9 Categories
- Example Output
- Assessment Process
- Rationalizations (Do Not Skip)
- Report Format
- Ready to Begin

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Systematic code maturity assessment using Aevrin Security's 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level... | First. Always. |
| `resources/ASSESSMENT_CRITERIA.md` | Focus: Overflow protection, precision handling, formula specification, edge case testing | When a step points to it, or when you need the detail. |
| `resources/EXAMPLE_REPORT.md` | When the assessment is complete, you'll receive a comprehensive maturity report: | When a step points to it, or when you need the detail. |
| `resources/REPORT_FORMAT.md` | Overall: [X.X / 4.0] | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.
- Report: Use plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/code-maturity-assessor.md with ratings, evidence, and recommended changes.
- Fix: Read ./reports/code-maturity-assessor.md. Apply the recommended changes one at a time, then check each one.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
