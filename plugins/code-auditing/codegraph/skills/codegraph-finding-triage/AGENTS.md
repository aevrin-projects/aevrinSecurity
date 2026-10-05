# Agent guide: codegraph-finding-triage

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/codegraph-finding-triage/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Performs graph-assisted triage of a single security finding, SARIF result, AuditNotes annotation, suspicious function, or report excerpt using Codegraph reachability, entrypoint paths, taint, privilege-boundary, blast-radius, caller/callee, and neighborhood evidence. Use when deciding whether one candidate issue is reachable, prioritizing a finding before PoC work, preparing evidence for exploit validation, or checking whether a static-analysis result is actionable.

## Use this skill when

- Triage one static-analysis result before spending PoC time
- Check whether a manual finding is entrypoint-reachable
- Build an evidence packet for PoC work
- Review a single suspicious function discovered during manual audit
- Decide whether one issue should be promoted, deprioritized, or treated as

## Do not use this skill when

- Multiple weak findings might compose into a stronger chain. Use a chain or
- The user wants a full audit. Use an audit or design-review workflow instead.
- The user wants remediation verification for a known finding. Use a
- The target is a PR or branch diff. Use `graph-evolution` plus a differential
- No concrete finding, function, file/line, or suspicious sink exists yet. Use

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
- Example Prompts

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Performs graph-assisted triage of a single security finding, SARIF result, AuditNotes annotation, suspicious function, or report excerpt using Codegraph reachability, entrypoint paths, taint, privilege-boundary, blast-radius,... | First. Always. |
| `references/input-normalization.md` | Input Normalization: Normalize every request into one candidate record before graph analysis. | When a step points to it, or when you need the detail. |
| `references/output-format.md` | Output Format: Return a concise evidence packet. Use Markdown unless the user asks for JSON. | When a step points to it, or when you need the detail. |
| `references/query-recipes.md` | Query Recipes: Use these recipes after building a graph and running engine.preanalysis(). | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-finding-triage.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
