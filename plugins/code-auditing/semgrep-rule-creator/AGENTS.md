# Agent guide: semgrep-rule-creator plugin

Category: Code Auditing
Folder: plugins/code-auditing/semgrep-rule-creator/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Create custom Semgrep rules for detecting bug patterns and security vulnerabilities

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| semgrep-rule-creator | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. | `skills/semgrep-rule-creator/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/semgrep-rule.md` | Creates Semgrep rules with test-first methodology | Saved prompt. Say: "Follow plugins/code-auditing/semgrep-rule-creator/commands/semgrep-rule.md on the target." |
| `README.md` | Semgrep Rule Creator: Create production-quality Semgrep rules for detecting bug patterns and security vulnerabilities. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
