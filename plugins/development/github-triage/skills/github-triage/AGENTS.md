# Agent guide: github-triage

Plugin: github-triage (Development)
Skill folder: plugins/development/github-triage/skills/github-triage/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs - incrementally merging passing automated/bot PRs and maintainer-approved ones, and spawning review subagents for never-reviewed ones - then closes already-resolved issues with comments citing the resolving PR or commit, cross-links issues with their pending fix PRs, and assigns local-only priority and change-size estimates for everything outstanding. Use when triaging, grooming, or reviewing a repository's open issues and PRs.

## Use this skill when

- When the user runs `/github-triage` to groom or review a repository's open issues
- When an issue backlog has drifted: resolved work left open, fixes landed without
- When ready PRs have piled up (passing dependency bumps, approved-and-green PRs) or

## Do not use this skill when

- Do not invoke automatically. This skill performs irreversible GitHub writes
- Do not use to apply priority/effort *labels* on GitHub. Priority and size are
- Do not use as a substitute for a human's final merge decision - every merge is

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Core Principles
- Workflow
- Triage for OWNER/REPO (N open issues)
- Safety Rules
- Rationalizations to Reject

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs - incrementally merging passing automated/bot PRs and maintainer-approved ones, and spawning review subagents... | First. Always. |
| `references/reviewing-prs.md` | Reviewing open pull requests: Rubric for the PR-review subagents the github-triage skill spawns in Phase 2 for | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/github-triage/skills/github-triage/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
