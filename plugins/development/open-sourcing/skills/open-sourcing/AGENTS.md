# Agent guide: open-sourcing

Plugin: open-sourcing (Development)
Skill folder: plugins/development/open-sourcing/skills/open-sourcing/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source readiness", "choose a license for this project", or "set up release automation" ahead of a public launch. Provides a release-readiness workflow covering secrets hygiene, licensing, documentation, CI, and language-specific packaging.

## Use this skill when

- Making a private repository public
- Auditing an existing public repository for release quality ("make it
- Choosing a license for a project
- Setting up packaging, versioning, or release automation ahead of a public

## Do not use this skill when

- Routine development on an already-released project (no release event)
- Auditing third-party code for vulnerabilities (use a security-review skill)
- Publishing a package from a repository that will stay private - only the

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Workflow
- Final Review
- Additional Resources

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source readiness", "choose a license for this project", or "set up... | First. Always. |
| `references/aevrin.md` | Aevrin Security Profile: Apply this guidance in addition to the generic workflow when | When a step points to it, or when you need the detail. |
| `references/c-cpp.md` | C/C++ Release Practices: Use modern CMake. For new projects, | When a step points to it, or when you need the detail. |
| `references/go.md` | Go Release Practices: Use the standard go toolchain for everything. | When a step points to it, or when you need the detail. |
| `references/javascript.md` | JavaScript/TypeScript Release Practices: Support the active and maintenance Node.js LTS lines, and declare the floor | When a step points to it, or when you need the detail. |
| `references/licensing.md` | Choosing and Applying an Open-Source License: A repository is not open source until it has a license. Without one, default | When a step points to it, or when you need the detail. |
| `references/python.md` | Python Release Practices: For project scaffolding, dependency management (uv), formatting/linting | When a step points to it, or when you need the detail. |
| `references/ruby.md` | Ruby Release Practices: Ruby releases a minor version yearly and the community supports roughly the | When a step points to it, or when you need the detail. |
| `references/rust.md` | Rust Release Practices: Use cargo for everything: building, testing (cargo test), formatting | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/open-sourcing/skills/open-sourcing/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
