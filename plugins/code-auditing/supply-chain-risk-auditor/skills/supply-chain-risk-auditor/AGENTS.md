# Agent guide: supply-chain-risk-auditor

Plugin: supply-chain-risk-auditor (Code Auditing)
Skill folder: plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution. Use when asked to audit dependencies, assess supply-chain or third-party package risk, or review a dependency tree before an engagement.

## Do not use this skill when

- License compliance auditing.
- Scanning the target's own source for vulnerabilities or secrets - this skill never
- Judging whether the project installs or builds. The audit is designed to work from
- Ecosystems other than npm, PyPI, and Go; say the ecosystem is unsupported rather than

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Why the scripts do the measuring, not you
- Workflow
- Style for what you add
- Reading the report
- Rationalizations to reject
- When not to use

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script... | First. Always. |

## Example requests

- Find: Use plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md. Scan the dependencies of this project. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md. Scan the dependencies of this project. Write a detailed report to ./reports/supply-chain-risk-auditor.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/supply-chain-risk-auditor.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
