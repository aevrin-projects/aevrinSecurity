# Agent guide: audit-augmentation

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/audit-augmentation/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Augments Codegraph code graphs with external audit findings from SARIF static analysis results, AuditNotes annotation files, and version-gated Codegraph 0.4.x binary-analysis graph exports. Maps findings to graph nodes by file and line overlap, creates severity-based subgraphs, and enables cross-referencing findings with pre-analysis data (blast radius, taint, etc.). Use when projecting SARIF results onto a code graph, overlaying AuditNotes annotations, importing binary graph findings, cross-referencing Semgrep, CodeQL, or binary-analysis findings with call graph data, or visualizing audit findings in the context of code structure.

## Use this skill when

- Importing Semgrep, CodeQL, or other SARIF-producing tool results into a graph
- Importing AuditNotes audit annotations into a graph
- Importing binary-analysis graph data into a source graph (Codegraph 0.4.0+)
- Cross-referencing static analysis findings with blast radius or taint data
- Querying which functions have high-severity findings
- Visualizing audit coverage alongside code structure
- Preparing one SARIF or AuditNotes result for `codegraph-finding-triage`

## Do not use this skill when

- Running static analysis tools (use semgrep/codeql directly, then import)
- Building the code graph itself (use the `codegraph` skill)
- Generating diagrams (use the `diagramming-code` skill after augmenting)

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
- Installation
- Version Gate
- Quick Start
- Workflow
- Annotation Format
- Subgraphs Created
- How Matching Works
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Augments Codegraph code graphs with external audit findings from SARIF static analysis results, AuditNotes annotation files, and version-gated Codegraph 0.4.x binary-analysis graph exports. Maps findings to graph nodes by file... | First. Always. |
| `references/formats.md` | SARIF and AuditNotes Format Reference: SARIF (Static Analysis Results Interchange Format) is an OASIS standard for | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md on this repository. Write the result and the evidence to ./reports/audit-augmentation.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
