# Agent guide: risky-apis

Plugin: risky-apis (Code Auditing)
Skill folder: plugins/code-auditing/risky-apis/skills/risky-apis/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

## Use this skill when

- Reviewing API or library design decisions
- Auditing configuration schemas for dangerous options
- Evaluating cryptographic API ergonomics
- Assessing authentication/authorization interfaces
- Reviewing any code that exposes security-relevant choices to developers

## Do not use this skill when

- Implementation bugs (use standard code review)
- Business logic flaws (use domain-specific analysis)
- Performance optimization (different concern)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Agent
- Core Principle
- Rationalizations to Reject
- Sharp Edge Categories
- Analysis Workflow
- Severity Classification
- References
- Quality Checklist

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code... | First. Always. |
| `references/auth-patterns.md` | Authentication & Session Footguns: Patterns that make authentication and session management error-prone. | When a step points to it, or when you need the detail. |
| `references/case-studies.md` | Real-World Case Studies: Analysis of sharp edges in widely-used libraries. These aren't implementation bugs-they're design decisions that make secure usage difficult. | When a step points to it, or when you need the detail. |
| `references/config-patterns.md` | Configuration Security Patterns: Dangerous configuration patterns that enable security failures. | When a step points to it, or when you need the detail. |
| `references/crypto-apis.md` | Cryptographic API Footguns: Detailed patterns for identifying misuse-prone cryptographic interfaces. | When a step points to it, or when you need the detail. |
| `references/lang-c.md` | C/C++ Sharp Edges: The Problem: Signed integer overflow is undefined behavior. Compilers assume it never happens and optimize accordingly-including removing overflow checks. | When a step points to it, or when you need the detail. |
| `references/lang-csharp.md` | C# Sharp Edges: Fix: Enable NRT AND treat warnings as errors: | When a step points to it, or when you need the detail. |
| `references/lang-go.md` | Go Sharp Edges: The Problem: Unlike Rust (debug panics), Go silently wraps. Fuzzing with go-fuzz may never find overflow bugs because they don't crash. | When a step points to it, or when you need the detail. |
| `references/lang-java.md` | Java Sharp Edges: Fix: Always use .equals() for object comparison: | When a step points to it, or when you need the detail. |
| `references/lang-javascript.md` | JavaScript / TypeScript Sharp Edges: Fix: Always use === for strict equality. | When a step points to it, or when you need the detail. |
| `references/lang-kotlin.md` | Kotlin Sharp Edges: Fix: Explicitly declare nullability when calling Java: | When a step points to it, or when you need the detail. |
| `references/lang-php.md` | PHP Sharp Edges: Fix: Use strict comparison ===: | When a step points to it, or when you need the detail. |
| `references/lang-python.md` | Python Sharp Edges: The Problem: Default arguments are evaluated once at function definition, not at each call. | When a step points to it, or when you need the detail. |
| `references/lang-ruby.md` | Ruby Sharp Edges: Real Vulnerabilities: | When a step points to it, or when you need the detail. |
| `references/lang-rust.md` | Rust Sharp Edges: The Problem: Behavior differs between debug and release. Bugs may only manifest in production. | When a step points to it, or when you need the detail. |
| `references/lang-swift.md` | Swift Sharp Edges: Fix: Use optional binding or nil-coalescing: | When a step points to it, or when you need the detail. |
| `references/language-specific.md` | Language-Specific Sharp Edges: General programming footguns by language-not limited to cryptography. | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md. Scan the APIs and configuration in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md. Scan the APIs and configuration in ./src. Write a detailed report to ./reports/risky-apis.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/risky-apis.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
