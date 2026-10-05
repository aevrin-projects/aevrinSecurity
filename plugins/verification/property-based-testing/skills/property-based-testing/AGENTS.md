# Agent guide: property-based-testing

Plugin: property-based-testing (Verification)
Skill folder: plugins/verification/property-based-testing/skills/property-based-testing/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Writes, reviews, and debugs property-based tests - Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input domain instead of a hand-picked list of examples: encode/decode and serialize/deserialize pairs, parsers, canonicalizers and normalizers, validators, numeric and Decimal types, comparators and sort order, data structures, and smart-contract state invariants. Also use when adding cases to an existing @given, fast-check, or proptest suite, when judging whether existing property tests assert anything real, and when a generator has shrunk a counterexample and you need to tell a wrong property from a genuine bug. Not for coverage-guided binary fuzzing (libFuzzer, AFL), mutation-testing campaigns, static analysis, benchmarking, or end-to-end UI tests.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Property catalog
- The two ways a property test asserts nothing
- Where to look next
- Introducing PBT to a project that lacks it

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Writes, reviews, and debugs property-based tests - Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input domain instead of a hand-picked... | First. Always. |
| `README.md` | Property-Based Testing Skill: Guidance for property-based testing across languages, including Echidna and Medusa for | Optional. For humans. |
| `references/generating.md` | Generating Property-Based Tests: Writing the @given decorator is the easy part. These are the decisions that make | When a step points to it, or when you need the detail. |
| `references/interpreting-failures.md` | Interpreting Property-Based Test Failures: A property test that fails has told you one of three things, and they need different | When a step points to it, or when you need the detail. |
| `references/libraries.md` | PBT Libraries by Language: Match the project's existing choice. Introducing a second PBT library into a codebase | When a step points to it, or when you need the detail. |
| `references/refactoring.md` | Refactoring to Expose a Property: "This code has no algebraic shape" is often a fact about how the code is *arranged* | When a step points to it, or when you need the detail. |
| `references/reviewing.md` | Reviewing Property-Based Tests: A property test can pass for years while asserting nothing. These are the ways that | When a step points to it, or when you need the detail. |

## Example requests

- Check: Use plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.
- Report: Use plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/property-based-testing.md with the verdict and the evidence for it.
- Fix: Read ./reports/property-based-testing.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
