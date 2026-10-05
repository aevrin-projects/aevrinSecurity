# Agent guide: post-patch-validation

Plugin: post-patch-validation (Verification)
Skill folder: plugins/verification/post-patch-validation/skills/post-patch-validation/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. Use after a patch exists and before accepting, merging, or reporting it as fixed; also use when an AI-generated patch, remediation commit, pull request, or proposed upstream fix needs adversarial post-patch validation across any language.

## Use this skill when

- A security fix, remediation commit, patch file, or pull request already exists.
- An AI-generated patch needs validation before human review or merge.
- A fix may cover one exploit path while missing variants of the same root cause.
- A security fix may alter legitimate behavior or introduce a new vulnerability.
- A patch author needs concrete failures and coverage gaps before another revision.

## Do not use this skill when

- No patch exists yet; use vulnerability discovery or fix implementation first.
- The task is to review an audit finding against a report without executing patch evidence.
- The task is only to convert a finding into a permanent project test.
- The target is remote or production. This skill executes local code and tests only.
- The user has not authorized execution of the repository's code or test suite.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Quick Start
- Evidence Contract
- Coverage Rules
- Reading the result
- Claude Dynamic Workflow
- Rationalizations to Reject

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. Use after a patch... | First. Always. |
| `references/evidence-model.md` | Evidence Model: Use this reference while authoring the validation plan or interpreting its result. | When a step points to it, or when you need the detail. |

## Example requests

- Check: Use plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.
- Report: Use plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/post-patch-validation.md with the verdict and the evidence for it.
- Fix: Read ./reports/post-patch-validation.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
