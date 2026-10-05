# Agent guide: diagramming-code

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/diagramming-code/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Generates Mermaid diagrams from Codegraph code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow visualizations. Use when visualizing code architecture, drawing call graphs, generating class diagrams, creating dependency maps, producing complexity heatmaps, or visualizing data flow and attack surface paths as Mermaid diagrams.

## Use this skill when

- Visualizing call paths between functions
- Drawing class inheritance hierarchies
- Mapping module import dependencies
- Showing class structure with members
- Highlighting complexity hotspots with color coding
- Tracing data flow from entrypoints to sensitive functions

## Do not use this skill when

- Querying the graph without visualization (use the `codegraph` skill)
- Mutation testing triage (use the `mutation-triage` skill)
- Architecture diagrams not derived from code (draw by hand)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Prerequisites
- Version Gate
- Quick Start
- Diagram Types
- Workflow
- Script Reference
- Customization
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Generates Mermaid diagrams from Codegraph code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow visualizations. Use when... | First. Always. |
| `references/diagram-types.md` | Diagram Types: Shows which functions call which. Built from callers_of / callees_of | When a step points to it, or when you need the detail. |
| `references/mermaid-syntax.md` | Mermaid Syntax Reference: Pitfalls and edge cases when generating Mermaid from code graph data. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md on this repository. Write the result and the evidence to ./reports/diagramming-code.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
