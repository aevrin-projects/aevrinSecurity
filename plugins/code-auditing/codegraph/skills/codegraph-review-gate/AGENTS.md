# Agent guide: codegraph-review-gate

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/codegraph-review-gate/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Runs a Codegraph structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed validation or authorization calls, privilege-boundary drift, blast-radius growth, complexity growth, and newly reachable sensitive sinks. Use when reviewing a PR, branch, remediation commit, or release diff where graph-level security regressions should be checked before merge.

## Use this skill when

- Reviewing a branch, pull request, release diff, or fix commit
- Checking whether a change expands attack surface
- Looking for removed validation or authorization on reachable paths
- Comparing before/after taint, privilege-boundary, blast-radius, or
- Producing graph evidence for a differential review

## Do not use this skill when

- Single-snapshot analysis. Use `codegraph` or `codegraph-structural`.
- Text-diff review only. Use `differential-review`.
- Full vulnerability discovery. Use an audit or bug-finding workflow.
- One static finding. Use `codegraph-finding-triage`.
- Tooling is unavailable and the user wants manual review only.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Rationalizations to Reject
- Workflow
- Requirements

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Runs a Codegraph structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed validation or authorization calls, privilege-boundary drift,... | First. Always. |
| `references/gate-rules.md` | Gate Rules: Start with deterministic, conservative rules. A triggered rule creates a | When a step points to it, or when you need the detail. |
| `references/output-format.md` | Output Format: Use Markdown unless the user asks for JSON. | When a step points to it, or when you need the detail. |
| `references/review-integration.md` | Review Integration: Use the review gate packet as supporting evidence for a human branch review. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-review-gate.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
