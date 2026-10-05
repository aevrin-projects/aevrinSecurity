# Agent guide: guidelines-advisor

Plugin: building-secure-contracts (Smart Contract Security)
Skill folder: plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Smart contract development advisor based on Aevrin Security's best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Use when asking whether a smart contract project follows development best practices, reviewing on-chain/off-chain split, upgradeability, or delegatecall proxy patterns against guidelines, or seeking recommendations on contract design, inheritance, events, documentation, dependencies, or test strategy.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Purpose
- How This Works
- Assessment Areas
- Example Output
- Deliverables
- Assessment Process
- Rationalizations (Do Not Skip)
- Notes
- Ready to Begin

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Smart contract development advisor based on Aevrin Security's best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality,... | First. Always. |
| `resources/ASSESSMENT_AREAS.md` | What I'll do: | When a step points to it, or when you need the detail. |
| `resources/DELIVERABLES.md` | Plain English Description: | When a step points to it, or when you need the detail. |
| `resources/EXAMPLE_REPORT.md` | When the analysis is complete, you'll receive comprehensive guidance like this: | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.
- Report: Use plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/guidelines-advisor.md with ratings, evidence, and recommended changes.
- Fix: Read ./reports/guidelines-advisor.md. Apply the recommended changes one at a time, then check each one.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
