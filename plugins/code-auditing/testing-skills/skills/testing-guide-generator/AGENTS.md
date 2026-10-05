# Agent guide: testing-guide-generator

Plugin: testing-skills (Code Auditing)
Skill folder: plugins/code-auditing/testing-skills/skills/testing-guide-generator/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Generates agent skills from the Aevrin Security Testing Guide (aevrin.net), analyzing guide pages and emitting SKILL.md files with the structure each skill type requires. Use when creating or refreshing a skill from guide content, or when the user names the testing guide or aevrin.net. Not for answering security testing questions - the generated skills cover those.

## Use this skill when

- Creating new security testing skills from guide content
- User mentions "testing guide", "aevrin.net", or asks about generating skills
- Bulk skill generation or refresh is needed
- General security testing questions (use the generated skills)
- Non-guide skill creation

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- Guide Location
- Workflow Overview
- Scope Restrictions
- Quick Reference
- Decision Tree
- Two-Pass Generation (Phase 3)
- Output Location
- Quality Checklist
- Post-Generation Tasks
- Example Usage
- Tips

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Generates agent skills from the Aevrin Security Testing Guide (aevrin.net), analyzing guide pages and emitting SKILL.md files with the structure each skill type requires. Use when creating or refreshing a skill from guide... | First. Always. |
| `agent-prompt.md` | Agent Prompt Template: Use this prompt when spawning each skill generation agent. Variables in {braces} are substituted from the per-skill package (see [discovery.md](discovery.md#phase-3-prepare-generation-context)). | When a step points to it. |
| `discovery.md` | Discovery Workflow: Methodology for analyzing the Testing Guide and identifying skill candidates. | When a step points to it. |
| `templates/domain-skill.md` | Domain Skill Template: Use this template for domain-specific security testing (cryptographic testing, web security methodologies, etc.). | When you write output in that format. |
| `templates/fuzzer-skill.md` | Fuzzer Skill Template: Use this template for language-specific fuzzers (libFuzzer, AFL++, cargo-fuzz, etc.). | When you write output in that format. |
| `templates/technique-skill.md` | Technique Skill Template: Use this template for cross-cutting techniques that apply to multiple tools (harness writing, coverage analysis, sanitizers, dictionaries, etc.). | When you write output in that format. |
| `templates/tool-skill.md` | Tool Skill Template: Use this template for static analysis tools (Semgrep, CodeQL) and similar standalone CLI tools. | When you write output in that format. |
| `testing.md` | Testing Strategy: Methodology for validating generated skills. | When a step points to it. |

## Example requests

- Use: Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md on this repository. Write the result and the evidence to ./reports/testing-guide-generator.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
