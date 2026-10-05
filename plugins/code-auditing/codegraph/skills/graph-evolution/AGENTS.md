# Agent guide: graph-evolution

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/graph-evolution/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Compares Codegraph code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint propagation changes, and privilege boundary modifications that text diffs miss. Use when comparing code between commits or tags, analyzing structural evolution, detecting attack surface growth, reviewing what changed between audit snapshots, or finding security-relevant changes that text diffs miss.

## Use this skill when

- Comparing two git refs to understand what structurally changed
- Auditing a range of commits for security-relevant evolution
- Detecting new attack paths created by code changes
- Finding functions whose blast radius or complexity grew silently
- Identifying taint propagation changes across refactors
- Pre-release structural comparison (tag-to-tag or branch-to-branch)

## Do not use this skill when

- Line-level code review (use `differential-review` for text-diff analysis)
- Single-snapshot analysis (use the `codegraph` skill directly)
- Diagram generation from a single snapshot (use the `diagramming-code` skill)
- Mutation testing triage (use the `mutation-triage` skill)

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
- Prerequisites
- Quick Start
- Decision Tree
- Workflow
- Diff Reference
- Quality Checklist
- Integration
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Compares Codegraph code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint... | First. Always. |
| `references/evolution-metrics.md` | Evolution Metrics Reference: This document explains each structural metric the graph-evolution skill | When a step points to it, or when you need the detail. |
| `references/report-format.md` | Report Format Reference: Output format for graph-evolution reports. The report is a markdown file | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md on this repository. Write the result and the evidence to ./reports/graph-evolution.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
