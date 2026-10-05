# Agent guide: token-integration-analyzer

Plugin: building-secure-contracts (Smart Contract Security)
Skill folder: plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Token integration and implementation analyzer based on Aevrin Security's token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Use when integrating or accepting arbitrary ERC20/ERC721 tokens, auditing a token implementation for standards conformity, or assessing risk from weird tokens such as fee-on-transfer, rebasing, missing return values, or blocklists.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Purpose
- How This Works
- Assessment Categories
- Example Output
- EXECUTIVE SUMMARY
- 1. GENERAL CONSIDERATIONS
- 2. CONTRACT COMPOSITION
- 3. OWNER PRIVILEGES
- 4. ERC20 CONFORMITY
- 5. WEIRD TOKEN PATTERN ANALYSIS
- Rationalizations (Do Not Skip)
- Deliverables
- Ready to Begin

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Token integration and implementation analyzer based on Aevrin Security's token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract... | First. Always. |
| `resources/ASSESSMENT_CATEGORIES.md` | Assessment Categories Reference: This document contains detailed assessment criteria for token analysis. Each category includes what to check, analysis methods, and verification checklists. | When a step points to it, or when you need the detail. |
| `resources/REPORT_TEMPLATES.md` | Report Templates: This document contains report templates and deliverables formats for token integration analysis. | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.
- Report: Use plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/token-integration-analyzer.md with ratings, evidence, and recommended changes.
- Fix: Read ./reports/token-integration-analyzer.md. Apply the recommended changes one at a time, then check each one.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
