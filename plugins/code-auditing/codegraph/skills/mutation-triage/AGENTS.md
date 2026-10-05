# Agent guide: mutation-triage

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/mutation-triage/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Graph-informed mutation testing triage. Parses codebases with Codegraph, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circom-mutator and cairo-mutator), or using necessist.

## Use this skill when

- After mutation testing reveals survived mutants that need triage
- Identifying where unit tests would have the highest impact
- Finding functions that need fuzz harnesses instead of unit tests
- Prioritizing test improvements using data flow context
- Filtering out harmless mutants from actionable ones
- Finding unnecessary test statements that indicate weak assertions (necessist)

## Do not use this skill when

- Codebase has no existing test suite (write tests first)
- Pure documentation or configuration changes
- Single-file scripts with trivial logic

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
- Rationalizations to Reject
- Quick Start
- Workflow Overview
- Decision Tree
- Phase 1: Build Code Graph and Run Pre-Analysis
- Phase 2: Run Mutation Testing
- Phase 2b: Run Necessist (Optional)
- Phase 3: Triage Findings
- Output Format
- Summary
- Corroborated Findings
- False Positives
- Missing Test Coverage

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Graph-informed mutation testing triage. Parses codebases with Codegraph, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing... | First. Always. |
| `references/graph-analysis.md` | Graph Analysis for Mutant Triage: How to use codegraph's code graph data to contextualize survived mutants | When a step points to it, or when you need the detail. |
| `references/mutation-frameworks.md` | Mutation Testing Frameworks: Language-specific setup, execution, and output parsing for mutation testing. | When a step points to it, or when you need the detail. |
| `references/triage-methodology.md` | Triage Methodology: Detailed criteria for classifying survived mutants into actionable buckets. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md on this repository. Write the result and the evidence to ./reports/mutation-triage.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
