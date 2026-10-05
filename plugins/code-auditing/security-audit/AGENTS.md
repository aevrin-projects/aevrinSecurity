# Agent guide: security-audit plugin

Category: Code Auditing
Folder: plugins/code-auditing/security-audit/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Source-first security audit workflow: reconnaissance, coverage-led hunting, adversarial validation, structured findings, and reports.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| security-audit | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits,... | `skills/security-audit/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Security Audit: The flagship Aevrin Security skill. It runs a structured, source-first security audit of a codebase and writes validated findings and reports. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
