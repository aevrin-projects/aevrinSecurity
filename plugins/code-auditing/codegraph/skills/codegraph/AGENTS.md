# Agent guide: codegraph

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/codegraph/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, entry point enumeration, proxy/unresolved-call tracking, type/reference queries, structural traversal, graph diffs, audit augmentation, declared cross-language/FFI/external links via `.codegraph/links.toml`, and SQL schema graphs. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, importing SARIF/AuditNotes/binary findings, linking source graphs across language or RPC boundaries, or building a code graph for audit prioritization. Feature-gate version-specific Codegraph APIs before using them; prefer `codegraph.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

## Use this skill when

- Mapping call paths from user input to sensitive functions
- Finding complexity hotspots for audit prioritization
- Identifying attack surface and entrypoints
- Understanding call relationships in unfamiliar codebases
- Security review or audit preparation across polyglot projects
- Adding LLM-inferred annotations (assumptions, preconditions) to code units
- Importing external binary-analysis graphs to connect source and binary views

## Do not use this skill when

- Single-file scripts where call graph adds no value (read the file directly)
- Architecture diagrams not derived from code (use the `diagramming-code` skill or draw by hand)
- Mutation testing triage (use the mutation-triage skill, which calls codegraph internally)
- Runtime behavior analysis (codegraph is static, not dynamic)

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
- Pre-Analysis Passes
- Language Selection
- Repository Links (v0.5+)
- Graph Model
- Key Concepts
- Query Patterns

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, entry point enumeration, proxy/unresolved-call... | First. Always. |
| `references/preanalysis-passes.md` | Pre-Analysis Passes: Four passes that enrich the code graph before downstream skills (mutation-triage, | When a step points to it, or when you need the detail. |
| `references/query-patterns.md` | Codegraph Query Patterns for Security Analysis: Common patterns for using Codegraph in security reviews. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/codegraph/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/codegraph/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
