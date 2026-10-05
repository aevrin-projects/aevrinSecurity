# Agent guide: semgrep-rule-variant-creator plugin

Category: Code Auditing
Folder: plugins/code-auditing/semgrep-rule-variant-creator/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Creates language variants of existing Semgrep rules with proper applicability analysis and test-driven validation

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| semgrep-rule-variant-creator | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent... | `skills/semgrep-rule-variant-creator/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Semgrep Rule Variant Creator: A Claude Code skill for porting existing Semgrep rules to new target languages with proper applicability analysis and test-driven validation. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
