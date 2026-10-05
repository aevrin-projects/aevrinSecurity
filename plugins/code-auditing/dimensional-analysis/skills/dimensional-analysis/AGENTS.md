# Agent guide: dimensional-analysis

Plugin: dimensional-analysis (Code Auditing)
Skill folder: plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

## Use this skill when

- Annotating a codebase with unit/dimension comments (e.g., `D18{tok}`, `D27{UoA/tok}`)
- Performing dimensional analysis on DeFi protocols, financial code, or scientific computations
- Hunting for arithmetic bugs caused by unit mismatches, missing scaling, or precision loss
- Auditing codebases with mixed decimal precisions or fixed-point arithmetic

## Do not use this skill when

- Codebases with no numeric arithmetic or unit conversions - there is nothing to annotate
- Pure integer counting logic (loop indices, array lengths) with no physical or financial dimensions
- When you only need a quick spot-check of a single formula - read the code directly instead of running the full pipeline

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Execution Mode
- Scope and Coverage Guarantees
- Delegation Contract
- Workflow
- Reference Documentation
- Final Output
- Completion Checklist

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a... | First. Always. |
| `references/annotate.md` | Step 2: Annotate the Codebase: After defining dimensions (Step 1), add annotations to all numeric values in the code. | When a step points to it, or when you need the detail. |
| `references/bug-patterns.md` | Dimensional Bug Patterns: This document catalogs common dimensional bugs with examples and detection strategies. Examples use Solidity syntax, but these bug patterns occur in any language performing arithmetic with mixed units... | When a step points to it, or when you need the detail. |
| `references/common-dimensions.md` | Common Dimensions in DeFi: This document catalogs standard dimensional units used across DeFi protocols. While examples use Solidity syntax, the dimensional vocabulary is protocol-agnostic and applies equally to Rust (Anchor,... | When a step points to it, or when you need the detail. |
| `references/dimension-algebra.md` | Dimensional Algebra Rules: This document defines the rules for dimensional arithmetic. While examples use Solidity syntax, these algebraic rules are universal and apply to any language performing fixed-point or scaled arithmetic. | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md. Scan the contracts or formulas in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md. Scan the contracts or formulas in ./src. Write a detailed report to ./reports/dimensional-analysis.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/dimensional-analysis.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
