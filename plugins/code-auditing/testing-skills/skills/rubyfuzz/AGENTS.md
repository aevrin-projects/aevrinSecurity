# Agent guide: rubyfuzz

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/rubyfuzz/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Sets up and runs Rubyfuzz, a coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and the native C extensions in gems, and sanitizer builds. Use when fuzzing a Ruby library or gem, testing a Ruby C extension for memory safety, or asking how to fuzz Ruby at all.

## Use this skill when

- Fuzzing Ruby applications or libraries
- Testing Ruby C extensions for memory safety issues
- You need coverage-guided fuzzing for Ruby code
- Working with Ruby gems that have native extensions

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
- Compilation
- Running Campaigns
- Sanitizer Integration
- Real-World Examples
- Troubleshooting
- Related Skills
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Sets up and runs Rubyfuzz, a coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and the native C extensions in gems, and sanitizer builds. Use when... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md on this repository. Write the result and the evidence to ./reports/rubyfuzz.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
