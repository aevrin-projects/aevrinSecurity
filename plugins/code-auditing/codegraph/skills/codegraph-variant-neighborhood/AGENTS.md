# Agent guide: codegraph-variant-neighborhood

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Expands one confirmed or suspected vulnerability into a Codegraph graph neighborhood of variant candidates by finding sibling functions, shared callers and callees, common sensitive sinks, common entrypoint paths, interface implementations, override relationships, type/reference neighbors, and structurally similar nodes. Use after one issue is found to seed similar-bug-finder, semgrep-rule-creator, static-analysis, or manual review with graph-derived candidate locations.

## Use this skill when

- A finding is confirmed or plausible and variants may exist
- The vulnerable pattern depends on call context
- The issue involves a shared sink, source, validator, interface, override,
- The next step is to seed `similar-bug-finder`, `semgrep-rule-creator`,

## Do not use this skill when

- No seed issue exists. Use discovery or triage first.
- The pattern is purely syntactic and already obvious. Use
- The question is exploit-chain composition across multiple findings. Use a
- The goal is remediation verification. Use a remediation-review workflow.
- The seed cannot be bound to a graph node.

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
- Stop Conditions

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Expands one confirmed or suspected vulnerability into a Codegraph graph neighborhood of variant candidates by finding sibling functions, shared callers and callees, common sensitive sinks, common entrypoint paths, interface... | First. Always. |
| `references/neighborhood-patterns.md` | Neighborhood Patterns: Use multiple bounded graph dimensions. Each dimension creates candidate review | When a step points to it, or when you need the detail. |
| `references/output-format.md` | Output Format: Use Markdown unless the user asks for JSON. | When a step points to it, or when you need the detail. |
| `references/ranking.md` | Ranking: Rank candidates by review value, not by confirmed severity. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-variant-neighborhood.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
