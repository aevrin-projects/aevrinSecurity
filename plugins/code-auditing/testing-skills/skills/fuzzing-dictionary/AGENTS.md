# Agent guide: fuzzing-dictionary

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers, binaries, and specifications, dictionary syntax, and wiring one into libFuzzer or AFL++. Use when fuzzing a parser, protocol, or file format, when coverage stalls at input validation, or when a target compares against fixed strings.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Overview
- When to Apply
- Quick Reference
- Step-by-Step
- Common Patterns
- Advanced Usage
- Anti-Patterns
- Tool-Specific Guidance
- Troubleshooting
- Related Skills
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers, binaries, and specifications, dictionary syntax, and wiring... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md on this repository. Write the result and the evidence to ./reports/fuzzing-dictionary.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
