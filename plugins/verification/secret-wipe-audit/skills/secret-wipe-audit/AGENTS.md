# Agent guide: secret-wipe-audit

Plugin: secret-wipe-audit (Verification)
Skill folder: plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

## Use this skill when

- Auditing cryptographic implementations (keys, seeds, nonces, secrets)
- Reviewing authentication systems (passwords, tokens, session data)
- Analyzing code that handles PII or sensitive credentials
- Verifying secure cleanup in security-critical codebases
- Investigating memory safety of sensitive data handling

## Do not use this skill when

- General code review without security focus
- Performance optimization (unless related to secure wiping)
- Refactoring tasks not related to sensitive data
- Code without identifiable secrets or sensitive values

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- How to Run
- Purpose
- Scope
- Inputs
- Prerequisites
- Approved Wipe APIs
- Finding Capabilities
- Agent Architecture
- Cross-Reference Convention
- Detection Strategy
- Output Format
- Confidence Gating
- Fix Recommendations
- Rationalizations to Reject

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling... | First. Always. |
| `prompts/report_template.md` | Zeroize Audit Report: Run ID: <run_id> | When a step points to it. |
| `prompts/system.md` | secret-wipe-audit (Agent Skill): Audits C/C++/Rust code for missing zeroization and compiler-removed wipes. | When a step points to it. |
| `prompts/task.md` | Task: Run secret-wipe-audit. | When a step points to it. |
| `references/compile-commands.md` | Working with compile_commands.json: This reference covers how to generate and use compile_commands.json for the secret-wipe-audit IR/ASM analysis pipeline. Read this before running Step 7 (IR comparison) or Step 8 (assembly... | When a step points to it, or when you need the detail. |
| `references/detection-strategy.md` | Detection Strategy: Read this during execution to guide per-step analysis. Steps 1-6 are Phase 1 (source-level); Steps 7-12 are Phase 2 (compiler-level). | When a step points to it, or when you need the detail. |
| `references/ir-analysis.md` | LLVM IR Analysis for Zeroization Auditing: This reference covers multi-level IR analysis for detecting compiler-optimized zeroization (dead-store elimination of wipes) and interpreting results. Read this during Step 7 (IR... | When a step points to it, or when you need the detail. |
| `references/mcp-analysis.md` | MCP-Assisted Semantic Analysis: This reference covers how to configure, query, and interpret Serena MCP evidence during the secret-wipe-audit semantic pass. For compile DB generation and flag extraction, refer to the... | When a step points to it, or when you need the detail. |
| `references/poc-generation.md` | PoC Crafting Reference: Each secret-wipe-audit finding is demonstrated with a bespoke proof-of-concept program | When a step points to it, or when you need the detail. |
| `references/rust-zeroization-patterns.md` | Rust Zeroization Patterns Reference: This reference documents vulnerability pattern detected by the secret-wipe-audit tooling for Rust code. | When a step points to it, or when you need the detail. |
| `workflows/phase-0-preflight.md` | Phase 0 - Preflight, Configuration, and Work Directory: None - this is the first phase. | At the phase it belongs to. |
| `workflows/phase-1-source-analysis.md` | Phase 1 - MCP Resolution and Source Analysis: Skip if mcp_mode=off or routing.mcp_available=false or language_mode=rust (MCP is C/C++ only). | At the phase it belongs to. |
| `workflows/phase-2-compiler-analysis.md` | Phase 2 - Compiler Analysis: Skip if language_mode=rust or tu-map.json has no C/C++ entries. | At the phase it belongs to. |
| `workflows/phase-3-interim-report.md` | Phase 3 - Interim Finding Collection: Spawn agent secret-wipe-audit:4-report-assembler via Task (subagent_type: "secret-wipe-audit:4-report-assembler") with: | At the phase it belongs to. |
| `workflows/phase-4-poc-generation.md` | Phase 4 - PoC Generation: Spawn agent secret-wipe-audit:5-poc-generator via Task (subagent_type: "secret-wipe-audit:5-poc-generator") with: | At the phase it belongs to. |
| `workflows/phase-5-poc-validation.md` | Phase 5 - PoC Validation & Verification: Spawn agent secret-wipe-audit:5b-poc-validator via Task (subagent_type: "secret-wipe-audit:5b-poc-validator") with: | At the phase it belongs to. |
| `workflows/phase-6-final-report.md` | Phase 6 - Report Finalization: Spawn agent secret-wipe-audit:4-report-assembler via Task (subagent_type: "secret-wipe-audit:4-report-assembler") with: | At the phase it belongs to. |
| `workflows/phase-7-test-generation.md` | Phase 7 - Test Generation: Spawn agent secret-wipe-audit:6-test-generator via Task (subagent_type: "secret-wipe-audit:6-test-generator") with: | At the phase it belongs to. |

## Example requests

- Find: Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md. Scan the C/C++ or Rust code that handles secrets in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md. Scan the C/C++ or Rust code that handles secrets in ./src. Write a detailed report to ./reports/secret-wipe-audit.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/secret-wipe-audit.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
