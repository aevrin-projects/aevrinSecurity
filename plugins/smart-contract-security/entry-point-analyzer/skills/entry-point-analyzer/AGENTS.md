# Agent guide: entry-point-analyzer

Plugin: entry-point-analyzer (Smart Contract Security)
Skill folder: plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

## Use this skill when

- Starting a smart contract security audit to map the attack surface
- Asked to find entry points, external functions, or audit flows
- Analyzing access control patterns across a codebase
- Identifying privileged operations and role-restricted functions
- Building an understanding of which functions can modify contract state

## Do not use this skill when

- Vulnerability detection (use code-understanding or domain-specific-audits)
- Writing exploit POCs (use solidity-poc-builder)
- Code quality or gas optimization analysis
- Non-smart-contract codebases
- Analyzing read-only functions (this skill excludes them)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Scope: State-Changing Functions Only
- Workflow
- Slither Integration (Solidity)
- Language Detection
- Access Classification
- Output Format
- Summary
- Public Entry Points (Unrestricted)
- Role-Restricted Entry Points
- Restricted (Review Required)
- Contract-Only (Internal Integration Points)
- Files Analyzed
- Filtering
- Analysis Guidelines

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted,... | First. Always. |
| `references/cosmwasm.md` | CosmWasm Entry Point Detection: | When a step points to it, or when you need the detail. |
| `references/move-aptos.md` | Move Entry Point Detection (Aptos): In Move, public functions can be invoked from transaction scripts (Aptos) and typically modify state. In addition, all entry functions are entrypoints. Package-protected (public package) and... | When a step points to it, or when you need the detail. |
| `references/move-sui.md` | Move Entry Point Detection (Sui): In Move, public functions can be invoked from programmable transaction blocks (Sui) or transaction scripts (Aptos) and typically modify state. In addition, private entry functions are... | When a step points to it, or when you need the detail. |
| `references/solana.md` | Solana Entry Point Detection: In Solana, most program instructions modify state. Exclude view-only patterns: | When a step points to it, or when you need the detail. |
| `references/solidity.md` | Solidity Entry Point Detection: | When a step points to it, or when you need the detail. |
| `references/ton.md` | TON Entry Point Detection (FunC/Tact): Focus on message handlers that modify state. Exclude read-only patterns: | When a step points to it, or when you need the detail. |
| `references/vyper.md` | Vyper Entry Point Detection: | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md. Scan the smart contracts in ./contracts. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md. Scan the smart contracts in ./contracts. Write a detailed report to ./reports/entry-point-analyzer.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/entry-point-analyzer.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
