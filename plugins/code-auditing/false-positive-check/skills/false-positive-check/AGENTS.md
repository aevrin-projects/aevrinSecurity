# Agent guide: false-positive-check

Plugin: false-positive-check (Code Auditing)
Skill folder: plugins/code-auditing/false-positive-check/skills/false-positive-check/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use when asked whether a specific finding is real, exploitable, or a false positive, or to verify or validate a suspected vulnerability - not for hunting or discovering new bugs.

## Use this skill when

- "Is this bug real?" or "is this a true positive?"
- "Is this a false positive?" or "verify this finding"
- "Check if this vulnerability is exploitable"
- Any request to verify or validate a specific suspected bug

## Do not use this skill when

- Finding or hunting for bugs ("find bugs", "security analysis", "audit code")
- General code review for style, performance, or maintainability
- Feature development, refactoring, or non-security tasks
- When the user explicitly asks for a quick scan without verification

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Rationalizations to Reject
- Step 0: Understand the Claim and Context
- Route: Standard vs Deep Verification
- Batch Triage
- Final Summary
- References

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use when asked whether a specific finding is real,... | First. Always. |
| `references/bug-class-verification.md` | Bug-Class-Specific Verification: Different bug classes require different verification approaches. After classifying the bug in Step 0, apply the class-specific requirements below in addition to the generic verification phases. | When a step points to it, or when you need the detail. |
| `references/deep-verification.md` | Deep Verification: Full task-based verification for complex bugs. Use when routing from SKILL.md selects the deep path, or when standard verification escalates. | When a step points to it, or when you need the detail. |
| `references/evidence-templates.md` | Evidence Templates: Use these templates when documenting verification evidence for each bug. | When a step points to it, or when you need the detail. |
| `references/false-positive-patterns.md` | False Positive Patterns - Lessons Learned: Apply ALL items in this checklist to EACH potential bug during verification. | When a step points to it, or when you need the detail. |
| `references/gate-reviews.md` | Gate Reviews and Verdicts: Before reporting ANY bug as a vulnerability, all six gate reviews must pass. Evaluate these during the GATE REVIEW task after all phases are complete: | When a step points to it, or when you need the detail. |
| `references/standard-verification.md` | Standard Verification: Linear single-pass checklist for straightforward bugs. No task tracking - work through each step sequentially and document findings inline. | When a step points to it, or when you need the detail. |

## Example requests

- Check: Use plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.
- Report: Use plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/false-positive-check.md with the verdict and the evidence for it.
- Fix: Read ./reports/false-positive-check.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
