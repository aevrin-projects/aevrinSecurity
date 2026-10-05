# Agent guide: vector-forge

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/vector-forge/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

## Use this skill when

- Generating test vectors for cryptographic algorithms or protocols
- Evaluating how well existing test vectors cover an implementation
- Finding implementation code paths that no test vector exercises
- Creating Wycheproof-style cross-implementation test vectors
- Measuring the concrete coverage value of a test vector suite

## Do not use this skill when

- No implementations exist yet (need code to mutate)
- Single trivial implementation with no edge cases
- Testing application logic rather than algorithm implementations
- The algorithm has no public test vectors to compare against

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Prerequisites
- Rationalizations to Reject
- Workflow Overview
- Phase 1: Discovery
- Phase 2: Harness
- Phase 3: Baseline
- Phase 4: Escape Analysis (Graph-Informed Triage)
- Phase 5: Vector Generation
- Phase 6: Validation
- Output Format
- Quality Checklist
- Integration
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the... | First. Always. |
| `references/fault-simulation.md` | Fault Simulation via Limb-Width Reimplementation: Generate test vectors that catch carry propagation, modular | When a step points to it, or when you need the detail. |
| `references/lessons-learned.md` | Lessons Learned (BLS12-381 Case Study): Patterns observed during mutation testing of gnark-crypto (Go), | When a step points to it, or when you need the detail. |
| `references/mutation-frameworks.md` | Mutation Testing Frameworks: Language-specific setup, execution, and output parsing for mutation testing. | When a step points to it, or when you need the detail. |
| `references/report-template.md` | Vector Forge Report Template: Write the report to VECTOR_FORGE_REPORT.md in the working directory. | When a step points to it, or when you need the detail. |
| `references/vector-patterns.md` | Test Vector Patterns for Cryptographic Primitives: Patterns for designing test vectors that target specific code paths | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md on this repository. Write the result and the evidence to ./reports/vector-forge.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
