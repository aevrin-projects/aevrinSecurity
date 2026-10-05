# Agent guide: codegraph-structural

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/codegraph-structural/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Runs full Codegraph structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface, and version-gated Codegraph 0.4+/0.5+ data such as proxy counts, subgraph edges, type/reference summaries, and entrypoint attributes. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots, proxy nodes, type references.

## Use this skill when

- Vivisect Phase 1 needs full structural data (hotspots, taint, blast radius, privilege boundaries)
- Detailed pre-analysis passes for a specific target scope
- Generating complexity and taint data for audit prioritization
- Inspecting proxy/unresolved-call counts, subgraph edges, or type-reference

## Do not use this skill when

- Quick overview only (use `codegraph-summary` instead)
- Ad-hoc code graph queries (use the main `codegraph` skill directly)
- Target is a single small file where structural analysis adds no value

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
| `SKILL.md` | Runs full Codegraph structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface, and version-gated Codegraph 0.4+/0.5+ data such as proxy... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-structural.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
