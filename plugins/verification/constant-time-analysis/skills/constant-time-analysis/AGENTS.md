# Agent guide: constant-time-analysis

Plugin: constant-time-analysis (Verification)
Skill folder: plugins/verification/constant-time-analysis/skills/constant-time-analysis/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

## Use this skill when

- Implementing or reviewing a signature, encryption, KEM, or key derivation routine
- Code applies `/` or `%` to a value derived from a key, plaintext, nonce, or token
- The user mentions "constant-time", "timing attack", "side-channel", or "KyberSlash"
- Reviewing functions named `sign`, `verify`, `encrypt`, `decrypt`, `derive_key`

## Do not use this skill when

- **Measuring** timing variance on a running binary - use the `constant-time-testing` skill from the `testing-skills` plugin, which covers dudect and statistical approaches and may not be installed. This skill inspects compiler output statically and never executes the code under test.
- Non-cryptographic code, or crypto code where every input is public
- High-level API usage where a vetted library owns the constant-time guarantees
- Cache and other microarchitectural side channels - the assembly view cannot see them

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Language Routing
- Running the Analyzer
- Interpreting Results
- Triaging Findings
- Limitations
- Real-World Impact
- References

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++,... | First. Always. |
| `README.md` | Constant-Time Analysis Skill: A Claude Code skill that detects timing side-channel vulnerabilities in cryptographic code by analyzing assembly or bytecode output for dangerous instructions. | Optional. For humans. |
| `references/compiled.md` | Constant-Time Analysis: Compiled Languages: Analysis guidance for C, C++, Go, and Rust. These languages compile to native assembly, where timing side-channels are detected by scanning for variable-time CPU instructions. | When a step points to it, or when you need the detail. |
| `references/javascript.md` | Constant-Time Analysis: JavaScript and TypeScript: Analysis guidance for JavaScript and TypeScript. Uses V8 bytecode output from Node.js to detect timing-unsafe operations. | When a step points to it, or when you need the detail. |
| `references/kotlin.md` | Constant-Time Analysis: Kotlin: Analysis guidance for Kotlin targeting Android and JVM platforms. Kotlin compiles to JVM bytecode, sharing the same runtime characteristics as Java. | When a step points to it, or when you need the detail. |
| `references/php.md` | Constant-Time Analysis: PHP: Analysis guidance for PHP scripts. Uses the VLD extension or OPcache debug output to analyze Zend opcodes. | When a step points to it, or when you need the detail. |
| `references/python.md` | Constant-Time Analysis: Python: Analysis guidance for Python scripts. Uses the dis module to analyze CPython bytecode for timing-unsafe operations. | When a step points to it, or when you need the detail. |
| `references/ruby.md` | Constant-Time Analysis: Ruby: Analysis guidance for Ruby scripts. Uses YARV (Yet Another Ruby VM) instruction sequence dump to analyze bytecode for timing-unsafe operations. | When a step points to it, or when you need the detail. |
| `references/swift.md` | Constant-Time Analysis: Swift: Analysis guidance for Swift targeting iOS, macOS, watchOS, and tvOS. Swift compiles to native code, making it subject to the same CPU-level timing side-channels as C, C++, Go, and Rust. | When a step points to it, or when you need the detail. |
| `references/vm-compiled.md` | Constant-Time Analysis: VM-Compiled Languages: Analysis guidance for Java and C#. These languages compile to bytecode (JVM bytecode / CIL) that runs on a virtual machine with Just-In-Time (JIT) compilation to native code. | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md. Scan the cryptographic code in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md. Scan the cryptographic code in ./src. Write a detailed report to ./reports/constant-time-analysis.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/constant-time-analysis.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
