# Agent guide: similar-bug-finder

Plugin: similar-bug-finder (Code Auditing)
Skill folder: plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Hunts for the other instances of a bug already found - the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or bad pattern turns up in a specific file and the question becomes where else it occurs, including the bare conversational form ("are there others like this?", "is this the same bug?"). Also for generalizing one known instance into a CodeQL or Semgrep query for its whole pattern family, and for triaging a set of look-alike candidates against a known root cause. Not for initial discovery with no bug in hand.

## Use this skill when

- A vulnerability has been found and you need to search for similar instances
- Building or refining CodeQL/Semgrep queries for security patterns
- Performing systematic code audits after an initial issue discovery
- Analyzing how a single root cause manifests in different code paths

## Do not use this skill when

- Initial vulnerability discovery - use code-understanding or a domain-specific audit
- General code review with no known pattern to search for
- Writing fix recommendations - use issue-writer
- Understanding unfamiliar code - use code-understanding first

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- The Five Steps
- Running it as a Workflow
- What Makes Hunts Fail
- Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Hunts for the other instances of a bug already found - the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or bad pattern turns up in a specific file and the question becomes... | First. Always. |
| `references/reporting.md` | Reporting a Variant Hunt: Advice for the final stage. The report is written for a security engineer that is reviewing vulnerability variants. | When a step points to it, or when you need the detail. |
| `references/root-cause.md` | Root Cause and Expansion Axes: Strategy for the first stage of a variant hunt: turning one known bug into the set of | When a step points to it, or when you need the detail. |
| `references/searching.md` | Searching: The Abstraction Ladder: Strategy for the sweep stage. You have a root cause and one axis to search. The job is to | When a step points to it, or when you need the detail. |
| `references/triage.md` | Triage: Deciding Whether a Candidate Is Real: Strategy for the verification stage. You have candidate locations that resemble a known | When a step points to it, or when you need the detail. |
| `resources/variant-report-template.md` | Variant Analysis Report: Root Cause: [e.g., "User input reaches SQL query without parameterization"] | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md. Scan this repository, starting from the bug I describe. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md. Scan this repository, starting from the bug I describe. Write a detailed report to ./reports/similar-bug-finder.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/similar-bug-finder.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
