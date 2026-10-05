# Agent guide: entry-point-analyzer plugin

Category: Smart Contract Security
Folder: plugins/smart-contract-security/entry-point-analyzer/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level, and generates structured audit reports.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| entry-point-analyzer | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public,... | `skills/entry-point-analyzer/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/entry-points.md` | Identifies state-changing entry points in smart contracts | Saved prompt. Say: "Follow plugins/smart-contract-security/entry-point-analyzer/commands/entry-points.md on the target." |
| `README.md` | Entry Point Analyzer: An agent skill for systematically identifying state-changing entry points in smart contract codebases to guide security audits. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
