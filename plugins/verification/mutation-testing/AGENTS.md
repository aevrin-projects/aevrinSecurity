# Agent guide: mutation-testing plugin

Category: Verification
Folder: plugins/verification/mutation-testing/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or finding bugs from surviving mutations.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| mutation-testing | Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results,... | `skills/mutation-testing/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Mutation Testing: Configure mutation testing campaigns, explain what surviving mutations reveal about tests, and investigate potential bugs in the affected code. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
