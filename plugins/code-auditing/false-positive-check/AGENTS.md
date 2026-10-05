# Agent guide: false-positive-check plugin

Category: Code Auditing
Folder: plugins/code-auditing/false-positive-check/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Systematic false positive verification for security bug analysis with mandatory gate reviews

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| false-positive-check | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use when asked whether a... | `skills/false-positive-check/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/data-flow-analyzer.md` | Analyzes data flow from source to vulnerability sink, mapping trust boundaries, API contracts, environment protections, and cross-references. Spawned by false-positive-check during Phase 1 verification. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/false-positive-check/agents/data-flow-analyzer.md." |
| `agents/exploitability-verifier.md` | Verifies whether a suspected vulnerability is actually exploitable by proving attacker control, mathematical bounds, and race condition feasibility. Spawned by false-positive-check during Phase 2 verification. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/false-positive-check/agents/exploitability-verifier.md." |
| `agents/poc-builder.md` | Creates proof-of-concept exploits (pseudocode, executable, and unit tests) demonstrating a verified vulnerability, plus negative PoCs showing exploit preconditions. Spawned by false-positive-check during Phase 4 verification. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/false-positive-check/agents/poc-builder.md." |
| `README.md` | false-positive-check: A plugin that enforces systematic false positive verification when verifying suspected security bugs. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
