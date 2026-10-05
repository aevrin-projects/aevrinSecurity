# Agent guide: semgrep-rule-variant-creator

Plugin: semgrep-rule-variant-creator (Code Auditing)
Skill folder: plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Run it as a workflow
- The four phases
- Output
- Scope and reporting
- Rationalizations to Reject
- Quick Reference
- Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each... | First. Always. |
| `references/applicability-analysis.md` | Applicability Analysis: Phase 1 of the variant creation workflow. Before porting a rule, analyze whether the vulnerability pattern applies to the target language. | When a step points to it, or when you need the detail. |
| `references/language-syntax-guide.md` | Language Syntax Translation Guide: Guidance for translating Semgrep patterns between languages. This is NOT a pre-built mapping-use these principles to research and adapt patterns for your specific case. | When a step points to it, or when you need the detail. |
| `references/workflow.md` | Variant Creation Mechanics and Troubleshooting: The orchestration lives in workflows/port-rule-to-languages.js at the plugin root, which | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md on this repository. Write the result and the evidence to ./reports/semgrep-rule-variant-creator.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
