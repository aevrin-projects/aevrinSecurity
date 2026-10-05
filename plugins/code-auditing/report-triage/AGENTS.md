# Agent guide: report-triage plugin

Category: Code Auditing
Folder: plugins/code-auditing/report-triage/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Principled framework for triaging vulnerability reports using 7 brocards (rules of thumb). Evaluates incoming CVEs, bug bounty submissions, and security findings against structured dismissal/acceptance criteria before escalating to deeper analysis.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| report-triage | This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid", "review a security finding",... | `skills/report-triage/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | report-triage: Principled framework for triaging vulnerability reports using 7 brocards | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
