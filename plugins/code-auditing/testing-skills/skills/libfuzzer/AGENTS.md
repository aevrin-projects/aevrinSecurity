# Agent guide: libfuzzer

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/libfuzzer/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds, corpus and dictionary management, sanitizer integration, and campaign triage. Use when writing or debugging an LLVMFuzzerTestOneInput harness, starting fuzzing on a C/C++ library, choosing between libFuzzer and AFL++, or working out why a libFuzzer run finds nothing.

## Use this skill when

- You need a simple, quick setup for C/C++ code
- Project uses Clang for compilation
- Single-core fuzzing is sufficient initially
- Transitioning to AFL++ later is an option (harnesses are compatible)

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
- Corpus Management
- Running Campaigns
- Fuzzing Dictionary
- Coverage Analysis
- Sanitizer Integration
- Real-World Examples
- Advanced Usage
- Troubleshooting
- Related Skills
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds, corpus and dictionary management, sanitizer integration, and... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md on this repository. Write the result and the evidence to ./reports/libfuzzer.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
