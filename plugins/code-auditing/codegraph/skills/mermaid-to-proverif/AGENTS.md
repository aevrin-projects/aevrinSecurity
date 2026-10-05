# Agent guide: mermaid-to-proverif

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/mermaid-to-proverif/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

## Use this skill when

- User asks to formally verify a cryptographic protocol described as a Mermaid sequenceDiagram
- User wants to generate a ProVerif model (.pv file) from a protocol diagram
- User wants to prove secrecy, authentication, or forward secrecy properties
- Input is the output of the `crypto-protocol-diagram` skill

## Do not use this skill when

- No Mermaid sequenceDiagram exists yet - use `crypto-protocol-diagram` first to generate one
- User wants to verify properties of non-cryptographic systems (state machines, access control)
- User wants to run ProVerif on an existing .pv file - just run `proverif model.pv` directly

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
- Decision Tree
- Example
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to... | First. Always. |
| `examples/simple-handshake/diagram.md` | Simple Authenticated Key Exchange Sequence Diagram: | When you write output in that format. |
| `references/crypto-to-proverif-mapping.md` | Cryptographic Operation to ProVerif Mapping: Maps every Mermaid annotation produced by the crypto-protocol-diagram skill | When a step points to it, or when you need the detail. |
| `references/proverif-syntax.md` | ProVerif Syntax Reference: ProVerif models cryptographic protocols in the applied pi-calculus. This | When a step points to it, or when you need the detail. |
| `references/security-properties.md` | Security Properties in ProVerif: A guide to choosing and expressing the right security queries for a given | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md on this repository. Write the result and the evidence to ./reports/mermaid-to-proverif.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
