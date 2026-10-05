# Agent guide: wycheproof

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/wycheproof/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more. Covers loading test vectors, mapping result flags onto pass and fail expectations, and reading a failure. Use when testing a crypto implementation against known attacks, checking a library against standard test vectors, or investigating why two implementations disagree on the same input.

## Use this skill when

- Testing cryptographic implementations (AES-GCM, ECDSA, ECDH, RSA, etc.)
- Validating that crypto code handles edge cases correctly
- Verifying implementations against known attack vectors
- Setting up CI/CD for cryptographic libraries
- Auditing third-party crypto code for correctness
- Testing for timing side-channels (use constant-time testing tools instead)
- Finding new unknown bugs (use fuzzing instead)

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
- Testing Workflow
- Repository Structure
- Supported Algorithms
- Test File Structure
- Implementation Guide
- Common Vulnerabilities Detected
- Case Study: Elliptic npm Package
- Advanced Usage
- Related Skills
- Skill Dependency Map
- Resources
- Summary

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more. Covers loading test vectors, mapping result flags onto pass... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md on this repository. Write the result and the evidence to ./reports/wycheproof.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
