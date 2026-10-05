# Agent guide: supply-chain-risk-auditor plugin

Category: Code Auditing
Folder: plugins/code-auditing/supply-chain-risk-auditor/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Audit a project's npm, PyPI, and Go dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned upstreams, npm publisher concentration, and install scripts

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| supply-chain-risk-auditor | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration,... | `skills/supply-chain-risk-auditor/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Supply Chain Risk Auditor: Generate a supply-chain risk report for a project's direct dependencies across npm, | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
