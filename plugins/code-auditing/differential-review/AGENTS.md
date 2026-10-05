# Agent guide: differential-review plugin

Category: Code Auditing
Folder: plugins/code-auditing/differential-review/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Security-focused differential review of code changes with git history analysis and blast radius estimation

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| differential-review | Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting callers, checks test coverage... | `skills/differential-review/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/adversarial-modeler.md` | Models attacker perspectives and builds exploit scenarios for HIGH RISK code changes. Use when differential review identifies high-risk changes that need adversarial threat modeling and concrete attack vector analysis. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/differential-review/agents/adversarial-modeler.md." |
| `commands/diff-review.md` | Performs security-focused differential review of code changes | Saved prompt. Say: "Follow plugins/code-auditing/differential-review/commands/diff-review.md on the target." |
| `README.md` | Differential Review: Security-focused differential review of code changes with git history analysis and blast radius estimation. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
