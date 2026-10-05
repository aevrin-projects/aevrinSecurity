# Agent guide: agentic-actions-auditor plugin

Category: Code Auditing
Folder: plugins/code-auditing/agentic-actions-auditor/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations (Claude Code Action, Gemini CLI, OpenAI Codex, GitHub AI Inference)

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| agentic-actions-auditor | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where... | `skills/agentic-actions-auditor/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | agentic-actions-auditor: Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations. Detects misconfigurations and attack vectors specific to Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub... | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
