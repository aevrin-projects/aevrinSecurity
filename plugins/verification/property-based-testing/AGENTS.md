# Agent guide: property-based-testing plugin

Category: Verification
Folder: plugins/verification/property-based-testing/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Write, review, and triage property-based tests - Hypothesis, fast-check, proptest, and Echidna or Medusa for Solidity invariants

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| property-based-testing | Writes, reviews, and debugs property-based tests - Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input... | `skills/property-based-testing/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Property-Based Testing: Write, review, and triage property-based tests - Hypothesis, fast-check, proptest, and | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
