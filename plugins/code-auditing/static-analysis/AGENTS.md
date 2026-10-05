# Agent guide: static-analysis plugin

Category: Code Auditing
Folder: plugins/code-auditing/static-analysis/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Static analysis toolkit with CodeQL, Semgrep, and SARIF parsing for security vulnerability detection

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| codeql | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build codeql database", "SAST scan",... | `skills/codeql/SKILL.md` |
| sarif-parsing | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or... | `skills/sarif-parsing/SKILL.md` |
| semgrep | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which... | `skills/semgrep/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Static Analysis: A comprehensive static analysis toolkit with CodeQL, Semgrep, and SARIF parsing for security vulnerability detection. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
