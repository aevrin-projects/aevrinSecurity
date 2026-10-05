# Agent guide: dimensional-analysis plugin

Category: Code Auditing
Folder: plugins/code-auditing/dimensional-analysis/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol. Prevents dimensional mismatches and catches formula bugs early.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| dimensional-analysis | Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or... | `skills/dimensional-analysis/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/arithmetic-scanner.md` | Scans repo for files with dimensional arithmetic to scope discovery | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/arithmetic-scanner.md." |
| `agents/dimension-annotator.md` | Adds dimensional annotations to source code at anchor points using Reserve Protocol's format | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-annotator.md." |
| `agents/dimension-discoverer.md` | Discovers dimensional vocabulary for codebases by analyzing naming conventions and protocol patterns | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-discoverer.md." |
| `agents/dimension-propagator.md` | Propagates dimensional annotations through arithmetic and call chains, reporting mismatches found during propagation | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-propagator.md." |
| `agents/dimension-validator.md` | Validates dimensional consistency and detects dimensional bugs in annotated code | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-validator.md." |
| `README.md` | Dimensional Analysis Plugin: Add dimensional annotations to codebases and detect dimensional bugs. Uses an annotation format inspired by Reserve Protocol's Solidity conventions, but applicable to any language or protocol... | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
