# Agent guide: mutation-testing

Plugin: mutation-testing (Verification)
Skill folder: plugins/verification/mutation-testing/skills/mutation-testing/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or finding bugs from surviving mutations.

## Use this skill when

- Mentions "mutator", "mutator-sol", or "mutation testing"
- Wants to configure, scope, or speed up a mutation testing campaign
- Wants to analyze mutation results - surviving/uncaught mutants, equivalent mutants, kill rate
- Wants to use mutation results to find bugs in the source code

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Routing
- Essential Commands
- What Results Mean
- Interpreting Mutation Types

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or... | First. Always. |
| `references/blockchain-patterns.md` | Blockchain-Specific Patterns: Blockchain-specific mutation testing patterns for Solidity, FunC/Tolk, Move, and Solana Rust codebases. These patterns extend the general equivalence catalog and severity criteria; where they... | When a step points to it, or when you need the detail. |
| `references/equivalent-mutants.md` | Equivalent Mutant Catalog: Equivalent mutants are mutations that produce semantically identical behavior to the original code. They are false positives in mutation testing: no test can kill them because no observable... | When a step points to it, or when you need the detail. |
| `references/input-formats.md` | Input Format Examples: Parsing anchors for mutation testing tools with non-standard output formats. Most tools (mutmut, cargo-mutants, mutahunter) produce straightforward JSON or CSV that can be parsed directly from field... | When a step points to it, or when you need the detail. |
| `references/optimization-strategies.md` | Optimization Strategies: Apply these strategies before running a campaign when Phase 3 of the configuration workflow requires optimization (estimated >16 hours or user requests). | When a step points to it, or when you need the detail. |
| `references/report-template.md` | Mutation Testing Analysis Report: Project: [Project Name] | When a step points to it, or when you need the detail. |
| `references/severity-classification.md` | Severity Classification Guide: Severity depends on the impact type of the mutated code, not the mutation operator used. The same operator replacement carries different severity depending on whether it occurs in access control... | When a step points to it, or when you need the detail. |
| `workflows/analyzing-results.md` | Analyzing Mutation Testing Results: Analyzes mutation testing campaign results to identify testing gaps, classify surviving mutants by severity, filter equivalent mutants, and produce a structured report. | At the phase it belongs to. |
| `workflows/bug-hunter.md` | Bug Hunting with Mutation Testing: Uses mutation testing results as a map to untested code, then hunts for real bugs there. | At the phase it belongs to. |
| `workflows/configuration.md` | Configuration and Optimization Guide: Guide for configuring mutator and optimizing mutation testing performance before running a campaign. | At the phase it belongs to. |

## Example requests

- Check: Use plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.
- Report: Use plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/mutation-testing.md with the verdict and the evidence for it.
- Fix: Read ./reports/mutation-testing.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
