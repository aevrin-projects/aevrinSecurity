# Agent guide: report-triage

Plugin: report-triage (Code Auditing)
Skill folder: plugins/code-auditing/report-triage/skills/report-triage/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid", "review a security finding", "dismiss a vulnerability", "should we fix this CVE", "prioritize a vulnerability report", or needs to determine whether an incoming vulnerability report warrants investigation. Applies 7 brocards (rules of thumb) to systematically accept, dismiss, or request more information on vulnerability reports, or needs to filter raw findings from agentic vulnerability discovery pipelines before human review.

## Use this skill when

- Filtering findings from agentic vulnerability discovery pipelines
- Triaging findings during a ToB audit to decide which warrant
- Evaluating third-party CVEs or advisories against a codebase under
- Reviewing bug bounty submissions or external vulnerability reports
- Providing structured, defensible justification when recommending a

## Do not use this skill when

- **Hunting for new bugs during an audit** -- use other skills
- **Proving exploitability of a confirmed finding** -- use a
- **Triaging fuzzer crashes in C/C++** -- use a dedicated crash

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Pipeline Position
- Triage Workflow
- Output Format
- Triage Summary: [Report ID or Title]
- Rationalizations to Reject
- Detailed References

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid", "review a security finding", "dismiss a vulnerability",... | First. Always. |
| `references/brocards-detail.md` | Brocards for Vulnerability Triage -- Detailed Reference: Expanded explanations, concrete examples, and edge cases for each of the | When a step points to it, or when you need the detail. |

## Example requests

- Check: Use plugins/code-auditing/report-triage/skills/report-triage/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.
- Report: Use plugins/code-auditing/report-triage/skills/report-triage/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/report-triage.md with the verdict and the evidence for it.
- Fix: Read ./reports/report-triage.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
