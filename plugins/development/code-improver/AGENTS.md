# Agent guide: code-improver plugin

Category: Development
Folder: plugins/development/code-improver/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Improves code targets - skills, plugins, or a branch's changes - through an autonomous review-and-fix workflow with a pluggable reviewer (any installed skill or agent), a cross-round findings ledger, oscillation escalation, and a mechanical scope guard.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| code-improver | Runs an autonomous review-and-fix improvement loop over any code target - a skill, plugin, module, or directory - using a reviewer the user names: any installed skill or agent. Keeps a cross-round... | `skills/code-improver/SKILL.md` |
| pr-improver | Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the branch touched. Reviews are... | `skills/pr-improver/SKILL.md` |
| skill-improver | Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes stop converging, and a... | `skills/skill-improver/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/fixer.md` | Applies fixes for the blocking findings dispatched by the /code-improver:improve workflow and returns one verdict per finding (fixed, rejected, or deferred) under a hard scope and git-safety contract. Dispatched by the... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/development/code-improver/agents/fixer.md." |
| `README.md` | Code Improver Plugin: Improves a code target through an autonomous review→fix loop. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
