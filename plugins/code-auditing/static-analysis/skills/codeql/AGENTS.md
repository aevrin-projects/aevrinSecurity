# Agent guide: codeql

Plugin: static-analysis (Code Auditing)
Skill folder: plugins/code-auditing/static-analysis/skills/codeql/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build codeql database", "SAST scan", "taint analysis", "dataflow analysis", or "find vulnerabilities in this repo". Covers Python, JavaScript/TypeScript, Go, Java/Kotlin, C/C++, C#, Ruby, and Swift. Supports "run all" (security-and-quality + security-experimental) and "important only" (high-precision) scan modes, and creates data extension models for project-specific sources and sinks. For fast single-file pattern matching, or when no build is available for a compiled language, use the semgrep skill; to parse SARIF that already exists rather than produce it, use the sarif-parsing skill.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Essential Principles
- Each Bash call is a fresh shell
- Output Directory
- Quick Start
- Rationalizations to Reject
- Workflow Selection
- Reference Index
- Success Criteria

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build codeql database", "SAST scan", "taint analysis", "dataflow... | First. Always. |
| `references/build-fixes.md` | Build Fixes: Fixes to apply when a CodeQL database build method fails. Try these in order, then retry the current build method. Log each fix attempt. | When a step points to it, or when you need the detail. |
| `references/diagnostic-query-templates.md` | Diagnostic Query Templates: Language-specific QL queries for enumerating sources and sinks recognized by CodeQL. Used during the data extensions creation process. | When a step points to it, or when you need the detail. |
| `references/extension-yaml-format.md` | Data Extension YAML Format: YAML format for CodeQL data extension files. Used by the create-data-extensions workflow to model project-specific sources, sinks, and flow summaries. | When a step points to it, or when you need the detail. |
| `references/important-only-suite.md` | Important-Only Query Suite: In important-only mode, generate a custom .qls query suite file at runtime. This applies the same precision/severity filtering to all packs (official + third-party). | When a step points to it, or when you need the detail. |
| `references/language-details.md` | Language-Specific Guidance: Commands below assume $DB_NAME and $CODEQL_LANG from the build-database workflow. They | When a step points to it, or when you need the detail. |
| `references/macos-arm64e-workaround.md` | macOS arm64e Workaround: Methods for building CodeQL databases on macOS Apple Silicon when the arm64e/arm64 architecture mismatch causes SIGKILL (exit code 137) during build tracing. | When a step points to it, or when you need the detail. |
| `references/performance-tuning.md` | Performance Tuning: All three are set on codeql database analyze "$DB_NAME". CODEQL_RAM is an environment | When a step points to it, or when you need the detail. |
| `references/quality-assessment.md` | Quality Assessment: How to assess and improve CodeQL database quality after a successful build. | When a step points to it, or when you need the detail. |
| `references/ruleset-catalog.md` | Ruleset Catalog: Usage: codeql/<lang>-queries:codeql-suites/<lang>-security-extended.qls | When a step points to it, or when you need the detail. |
| `references/run-all-suite.md` | Run-All Query Suite: In run-all mode, generate a custom .qls query suite file at runtime. It runs the security-and-quality and security-experimental suites of every installed pack, which is a much wider selection than the... | When a step points to it, or when you need the detail. |
| `references/sarif-processing.md` | SARIF Processing: jq commands for processing CodeQL SARIF output. Used in the run-analysis workflow Step 5. | When a step points to it, or when you need the detail. |
| `references/threat-models.md` | Threat Models Reference: Control which source categories are active during CodeQL analysis. By default, only remote sources are tracked. | When a step points to it, or when you need the detail. |
| `workflows/build-database.md` | Build Database Workflow: Create high-quality CodeQL databases by trying build methods in sequence until one produces good results. | At the phase it belongs to. |
| `workflows/create-data-extensions.md` | Create Data Extensions Workflow: Generate data extension YAML files to improve CodeQL's data flow coverage for project-specific APIs. Runs after database build and before analysis. | At the phase it belongs to. |
| `workflows/run-analysis.md` | Run Analysis Workflow: Execute CodeQL security queries on an existing database with ruleset selection and result formatting. | At the phase it belongs to. |

## Example requests

- Find: Use plugins/code-auditing/static-analysis/skills/codeql/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/static-analysis/skills/codeql/SKILL.md. Scan this repository. Write a detailed report to ./reports/codeql.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/codeql.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
