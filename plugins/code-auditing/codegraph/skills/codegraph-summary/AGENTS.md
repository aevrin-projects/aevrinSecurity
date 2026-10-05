# Agent guide: codegraph-summary

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/codegraph-summary/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Runs a Codegraph summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: codegraph summary, code summary, structural overview.

## Use this skill when

- Vivisect Phase 0 needs a quick structural overview before decomposition
- Galvanize Phase 1 needs detected languages and entry point count
- Quick orientation on an unfamiliar codebase before deeper analysis

## Do not use this skill when

- Full structural analysis with all passes needed (use `codegraph-structural`)
- Detailed code graph queries (use the main `codegraph` skill directly)
- You need hotspot scores or taint data (use `codegraph-structural`)

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
- Usage
- Execution

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Runs a Codegraph summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: codegraph summary, code... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-summary.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
