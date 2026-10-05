# Agent guide: secure-workflow-guide

Plugin: building-secure-contracts (Smart Contract Security)
Skill folder: plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Guides through Aevrin Security's 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas. Use when securing a smart contract end to end rather than hunting one bug, checking a project on every check-in or before deployment, triaging a Slither report, or asking where to start on smart contract security.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Purpose
- The 5-Step Workflow
- How I Work
- Rationalizations (Do Not Skip)
- Example Output
- What You'll Get
- Getting Help
- Ready to Start

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Guides through Aevrin Security's 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security... | First. Always. |
| `resources/EXAMPLE_REPORT.md` | When I complete the workflow, you'll get a comprehensive security report: | When a step points to it, or when you need the detail. |
| `resources/WORKFLOW_STEPS.md` | I'll run Slither with 70+ built-in detectors: | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.
- Report: Use plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/secure-workflow-guide.md with ratings, evidence, and recommended changes.
- Fix: Read ./reports/secure-workflow-guide.md. Apply the recommended changes one at a time, then check each one.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
