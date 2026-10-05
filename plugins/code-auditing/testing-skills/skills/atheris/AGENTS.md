# Agent guide: atheris

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/atheris/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and native C extensions, and running under AddressSanitizer. Use when fuzzing a Python package, hunting memory corruption in a Python C extension, or choosing between Atheris and Hypothesis for a Python target.

## Use this skill when

- Fuzzing pure Python code with coverage guidance
- Testing Python C extensions for memory corruption
- Integration with libFuzzer ecosystem is desired
- AddressSanitizer support is needed

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- Quick Start
- Installation
- Writing a Harness
- Fuzzing Pure Python Code
- Fuzzing Python C Extensions
- Corpus Management
- Running Campaigns
- Sanitizer Integration
- Advanced Usage
- Real-World Examples
- Troubleshooting
- Related Skills
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and native C extensions, and running under AddressSanitizer. Use... | First. Always. |
| `examples.md` | Atheris Examples: Two complete harnesses, each runnable as written. | When a step points to it. |
| `structured-input.md` | Structured Input with FuzzedDataProvider: A target that takes several typed arguments - a string, a length, a flag - wastes most of | When a step points to it. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/atheris/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/atheris/SKILL.md on this repository. Write the result and the evidence to ./reports/atheris.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
