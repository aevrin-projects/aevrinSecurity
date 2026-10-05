# Agent guide: constant-time-testing

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/constant-time-testing/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing. Covers the formal, symbolic, dynamic, and statistical tool categories and how to read a result. Use when testing whether a running implementation is constant-time, measuring timing variance on a compiled binary, or investigating a suspected timing attack. Not for statically inspecting compiler output - the constant-time-analysis plugin covers that.

## Use this skill when

- Auditing cryptographic implementations (primitives, protocols)
- Code handles secret keys, passwords, or sensitive cryptographic material
- Implementing crypto algorithms from scratch
- Reviewing PRs that touch crypto code
- Investigating potential timing vulnerabilities
- Code does not process secret data
- Public algorithms with no secret inputs

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Background
- When to Use
- Quick Reference
- Constant-Time Tooling Categories
- Testing Workflow
- Tools and Approaches
- Implementation Guide
- Common Vulnerabilities
- Case Studies
- Advanced Usage
- Related Skills
- Skill Dependency Map
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing. Covers the formal, symbolic, dynamic, and statistical tool... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md on this repository. Write the result and the evidence to ./reports/constant-time-testing.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
