# Agent guide: modern-cpp

Plugin: modern-cpp (Development)
Skill folder: plugins/development/modern-cpp/skills/modern-cpp/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces raw pointers with smart pointers, SFINAE with concepts, printf with std::print, error codes with std::expected.

## Use this skill when

- Writing new C++ functions, classes, or libraries
- Modernizing existing C++ code (pre-C++20 patterns)
- Choosing between legacy and modern approaches
- Working on security-critical or safety-sensitive C++
- Reviewing C++ code for modern idiom adoption

## Do not use this skill when

- **User explicitly requires older standard**: Respect constraints (embedded, legacy ABI)
- **Pure C code**: This skill is C++-specific
- **Build system questions**: CMake, Meson, Bazel configuration is out of scope
- **Non-C++ projects**: Mixed codebases where C++ isn't primary

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use This Skill
- When NOT to Use This Skill
- Anti-Patterns to Avoid
- Decision Tree
- Feature Tiers
- Compiler Hardening Quick Reference
- Rationalizations to Reject
- Best Practices Checklist
- Read Next

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces raw pointers with smart pointers, SFINAE with concepts, printf with... | First. Always. |
| `references/anti-patterns.md` | Anti-Patterns: Legacy to Modern C++: Comprehensive reference of legacy C++ patterns and their modern replacements. Each entry explains WHY the modern version is better - not just that it exists. | When a step points to it, or when you need the detail. |
| `references/compiler-hardening.md` | Compiler Hardening: Security-focused compiler and linker configuration for C++ projects. Based on the [OpenSSF Compiler Options Hardening... | When a step points to it, or when you need the detail. |
| `references/cpp20-features.md` | C++20 Features (Default Practice): These features are mature, well-supported (GCC 12+, Clang 14+, MSVC 17.0+), and should be the default way to write C++. | When a step points to it, or when you need the detail. |
| `references/cpp23-features.md` | C++23 Features (Usable Today): These features have solid compiler support (GCC 13+, Clang 17+, MSVC 17.4+) and deliver immediate value. Adopt them now. | When a step points to it, or when you need the detail. |
| `references/cpp26-features.md` | C++26 Features: C++26 was finalized in March 2026 - the most significant release since C++11. This reference covers the features worth knowing about, ranked by practical impact. | When a step points to it, or when you need the detail. |
| `references/safe-idioms.md` | Safe C++ Idioms: Security patterns organized by vulnerability class. Each section explains what exploitable bugs the pattern prevents and what modern C++ features eliminate them. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/modern-cpp/skills/modern-cpp/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
