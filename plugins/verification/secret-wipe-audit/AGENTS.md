# Agent guide: secret-wipe-audit plugin

Category: Verification
Folder: plugins/verification/secret-wipe-audit/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Detects missing or compiler-optimized zeroization of sensitive data with assembly and control-flow analysis

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| secret-wipe-audit | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for... | `skills/secret-wipe-audit/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/0-preflight.md` | Performs preflight validation, config merging, TU enumeration, and work directory setup for secret-wipe-audit. Produces merged-config.yaml, preflight.json, and orchestrator-state.json. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/0-preflight.md." |
| `agents/1-mcp-resolver.md` | Resolves symbol definitions, types, and cross-file references using Serena MCP for secret-wipe-audit. Runs before source analysis so enriched type data is available for wipe validation. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/1-mcp-resolver.md." |
| `agents/2-source-analyzer.md` | Identifies sensitive objects, detects wipe calls, validates correctness, and performs data-flow/heap analysis for secret-wipe-audit. Produces the sensitive object list and source-level findings consumed by compiler analysis... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/2-source-analyzer.md." |
| `agents/2b-rust-source-analyzer.md` | Performs source-level zeroization analysis for Rust crates in secret-wipe-audit. Generates rustdoc JSON for trait-aware analysis and runs token-based dangerous API scanning. Produces sensitive objects and source findings... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/2b-rust-source-analyzer.md." |
| `agents/3-tu-compiler-analyzer.md` | Performs per-TU compiler-level analysis (IR diff, assembly, semantic IR, CFG) for secret-wipe-audit. One instance runs per translation unit, enabling parallel execution across TUs. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/3-tu-compiler-analyzer.md." |
| `agents/3b-rust-compiler-analyzer.md` | Performs crate-level MIR and LLVM IR analysis for Rust in secret-wipe-audit. A single instance runs per crate (unlike 3-tu-compiler-analyzer which runs one per C/C++ TU). Detects dead-store elimination of wipes, stack... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/3b-rust-compiler-analyzer.md." |
| `agents/4-report-assembler.md` | Collects all findings from source and compiler analysis, applies supersessions and confidence gates, normalizes IDs, and produces a comprehensive markdown report with structured JSON for downstream tools. Supports dual-mode... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/4-report-assembler.md." |
| `agents/5-poc-generator.md` | Crafts bespoke proof-of-concept programs demonstrating that secret-wipe-audit findings are exploitable. Reads source code and finding details to generate tailored PoCs - each PoC is individually written, not templated. Each... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/5-poc-generator.md." |
| `agents/5b-poc-validator.md` | Compiles and runs all PoCs for secret-wipe-audit findings. Produces poc_validation_results.json consumed by the verification agent and the orchestrator. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/5b-poc-validator.md." |
| `agents/5c-poc-verifier.md` | Verifies that each secret-wipe-audit PoC actually proves the vulnerability it claims to demonstrate. Reads PoC source code, finding details, and original source to check alignment between the PoC and the finding. Produces... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/5c-poc-verifier.md." |
| `agents/6-test-generator.md` | Generates runtime validation test harnesses (C tests, MSAN, Valgrind targets) for confirmed secret-wipe-audit findings. Produces a Makefile for automated test execution. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/6-test-generator.md." |
| `README.md` | secret-wipe-audit (Agent Skill): Audits C/C++/Rust code for missing zeroization and compiler-removed wipes. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
