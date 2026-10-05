# Agent guide: aflpp

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/aflpp/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode, corpus minimization, and crash triage. Use when scaling fuzzing across cores, fuzzing a mature C/C++ codebase, reading the afl-fuzz status screen, or moving on after libFuzzer has plateaued.

## Use this skill when

- You need multi-core fuzzing to maximize throughput
- Your project can be compiled with Clang or GCC
- You want diverse mutation strategies and mature tooling
- libFuzzer has plateaued and you need more coverage
- You're fuzzing production codebases that benefit from parallel execution

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
- Environment Variables That Matter
- Multi-Core Fuzzing
- Coverage Analysis
- CMPLOG
- Sanitizer Integration
- Advanced Usage
- Troubleshooting
- Related Skills
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode, corpus minimization, and crash... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md on this repository. Write the result and the evidence to ./reports/aflpp.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
