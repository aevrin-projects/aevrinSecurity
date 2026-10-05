# Agent guide: slicing-code-context

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/slicing-code-context/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Selects bounded, graph-informed source slices with Codegraph and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading function-, class-, caller-, callee-, call-path-, entrypoint-, or line-focused code tasks to constrained or locally hosted models without exposing the full repository.

## Use this skill when

- Offload explanation, classification, review, or mechanical edit proposals for a function or class
- Trace callers, callees, shortest call paths, or entrypoint-to-target paths within a small context window
- Focus a local or lower-cost model on explicit source lines and their graph neighborhood
- Keep repository access and final judgment with the coordinator

## Do not use this skill when

- The worker must explore the repository or discover its own scope
- Runtime behavior, generated code, macros, or dynamic dispatch dominate what Codegraph can see
- The anchor alone cannot fit and no meaningful line range is known
- The task requires direct worker edits; workers may only propose changes
- A small file can be read safely without graph selection or delegation

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
- Workflow
- Error Handling
- Example Requests
- Input to Output Example

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Selects bounded, graph-informed source slices with Codegraph and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading function-, class-, caller-, callee-, call-path-, entrypoint-,... | First. Always. |
| `references/slice-packet.md` | Slice Packet and Worker Contract: The slicer emits schema version 1.0 as JSON or Markdown. JSON is the preferred | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md on this repository. Write the result and the evidence to ./reports/slicing-code-context.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
