# Agent guide: writing-lean-proofs

Plugin: writing-lean-proofs (Verification)
Skill folder: plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or specifications in Lean 4, defining new types or definitions in a Lean library, reviewing Lean proofs for readability and maintainability, refactoring long tactic proofs into lemmas, filling in sorry placeholders in a Lean development, setting up CI or linters for a Lean project, diagnosing slow proofs or maxHeartbeats timeouts, or writing custom tactics, macros, or linters.

## Use this skill when

- Proving theorems in Lean 4, from single lemmas to multi-file developments
- Formalizing mathematics, protocols, or software specifications in Lean
- Defining new types, structures, or functions in a Lean library
- Reviewing Lean code for readability, maintainability, or Mathlib readiness
- Refactoring a long or fragile tactic proof into lemmas
- Setting up a formalization project that several people or agents will
- Setting up CI, linters, or verification gates for a Lean project - do this

## Do not use this skill when

- Lean 4 as a general-purpose programming language (no proofs involved) -
- Coq, Isabelle, Agda, or Lean 3 - conventions and tactic names differ;
- Verified-software Lean projects with their own house style (e.g.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Contents
- When to Use
- When NOT to Use
- The workflow
- The extraction ladder
- Quick reference
- Rationalizations to reject
- References

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or specifications in Lean 4, defining new types or definitions in... | First. Always. |
| `references/anti-patterns.md` | Anti-patterns: Each entry: what it is, why it is harmful (not just that it is), and which | When a step points to it, or when you need the detail. |
| `references/library-design.md` | Library design: definitions, APIs, and project decomposition: How Mathlib and the large formalization projects structure theory | When a step points to it, or when you need the detail. |
| `references/linting.md` | Linting: gates in CI early, custom linters for your own constructs: Set up an appropriate linter set, gated in CI, at the start of the project - and | When a step points to it, or when you need the detail. |
| `references/llm-techniques.md` | LLM-specific techniques: Techniques with direct evidence for model-written Lean, primarily from | When a step points to it, or when you need the detail. |
| `references/naming-conventions.md` | Naming conventions: Mathlib names are computable from statements. This matters doubly for LLMs: | When a step points to it, or when you need the detail. |
| `references/performance.md` | Elaboration and reduction cost: Slow proofs and heartbeat timeouts are measurement problems before they are | When a step points to it, or when you need the detail. |
| `references/proof-style.md` | Tactic proof style: How to structure the inside of a proof. Sources: Mathlib style and PR review | When a step points to it, or when you need the detail. |
| `references/tactics.md` | Writing tactics and metaprograms: Custom tactics, macros, simprocs, and elaborators have distinctive failure modes. A bug can | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md on this repository. Write the result and the evidence to ./reports/writing-lean-proofs.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
