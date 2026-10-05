# Agent guide: writing-lean-proofs plugin

Category: Verification
Folder: plugins/verification/writing-lean-proofs/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Structured Lean 4 proof writing and library design following Mathlib conventions

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| writing-lean-proofs | Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or specifications in Lean 4,... | `skills/writing-lean-proofs/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | writing-lean-proofs: Structured Lean 4 proof writing and library design following Mathlib | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
