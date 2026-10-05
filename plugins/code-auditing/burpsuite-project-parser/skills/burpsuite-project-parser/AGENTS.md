# Agent guide: burpsuite-project-parser

Plugin: burpsuite-project-parser (Code Auditing)
Skill folder: plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

## Use this skill when

- Searching response headers or bodies with regex patterns
- Extracting security audit findings from Burp projects
- Dumping proxy history or site map data
- Analyzing HTTP traffic captured in a Burp project file

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- Prerequisites
- Quick Reference
- Sub-Component Filters (USE THESE)
- Regex Search Operations
- Other Operations
- Output Limits (REQUIRED)
- Investigation Workflow
- Understanding Results
- Rationalizations to Reject
- Output Format
- Examples
- Platform Configuration

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or... | First. Always. |

## Example requests

- Use: Use plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md on this repository. Write the result and the evidence to ./reports/burpsuite-project-parser.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
