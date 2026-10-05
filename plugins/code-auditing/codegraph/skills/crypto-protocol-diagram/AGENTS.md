# Agent guide: crypto-protocol-diagram

Plugin: codegraph (Code Auditing)
Skill folder: plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

## Use this skill when

- User asks to diagram, visualize, or extract a cryptographic protocol
- Input is source code implementing a handshake, key exchange, or multi-party protocol
- Input is an RFC, academic paper, pseudocode, or formal model (ProVerif/Tamarin)
- User names a specific protocol (TLS, Noise, Signal, X3DH, FROST)

## Do not use this skill when

- User wants a call graph, class hierarchy, or module dependency map - use `diagramming-code`
- User wants to formally verify a protocol - use `mermaid-to-proverif` (after generating the diagram)
- Input has no cryptographic protocol semantics (no parties, no message exchange)

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
- Spec Workflow (S1-S5)
- Protocol Summary
- Decision Tree
- Examples
- Supporting Documentation

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when... | First. Always. |
| `examples/simple-handshake/expected-output.md` | Expected Skill Output: This file shows what the crypto-protocol-diagram skill should produce when | When you write output in that format. |
| `examples/simple-proverif/expected-output.md` | Expected Output: simple-proverif: This is the exact ASCII diagram and Mermaid file the crypto-protocol-diagram | When you write output in that format. |
| `references/ascii-sequence-diagram.md` | ASCII Sequence Diagram Reference: Rules for drawing ASCII sequence diagrams inline in responses. | When a step points to it, or when you need the detail. |
| `references/mermaid-sequence-syntax.md` | Mermaid Sequence Diagram Syntax Reference: Every sequence diagram starts with sequenceDiagram on its own line (no | When a step points to it, or when you need the detail. |
| `references/protocol-patterns.md` | Crypto Protocol Patterns Reference: Canonical message flows for common cryptographic protocols. Use these as a | When a step points to it, or when you need the detail. |
| `references/spec-parsing-patterns.md` | Spec Parsing Patterns Reference: Extraction rules for turning protocol specifications into sequence diagram | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md. Task: <describe what you want>. Target: this repository.
- Save the output: Use plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md on this repository. Write the result and the evidence to ./reports/crypto-protocol-diagram.md.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
