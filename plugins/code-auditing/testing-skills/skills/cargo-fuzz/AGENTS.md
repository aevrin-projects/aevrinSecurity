# Agent guide: cargo-fuzz

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/cargo-fuzz/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses, Arbitrary-derived structured inputs, sanitizer options, cargo fuzz coverage, and reproducing a crash artifact. Use when fuzzing a Rust crate, writing a fuzz_target!, exercising unsafe blocks or FFI in Rust, or triaging a cargo fuzz crash.

## Use this skill when

- Your project uses Cargo (required)
- You want simple, quick setup with minimal configuration
- You need integrated sanitizer support
- You're fuzzing Rust code with or without unsafe blocks

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
- Structure-Aware Fuzzing
- Running Campaigns
- Sanitizer Integration
- Coverage Analysis
- Advanced Usage
- Real-World Examples
- Troubleshooting
- Related Skills
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses, Arbitrary-derived structured inputs, sanitizer options,... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md on this repository. Write the result and the evidence to ./reports/cargo-fuzz.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
