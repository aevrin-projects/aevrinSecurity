# Agent guide: devcontainer-setup

Plugin: devcontainer-setup (Development)
Skill folder: plugins/development/devcontainer-setup/skills/devcontainer-setup/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

## Use this skill when

- User asks to "set up a devcontainer" or "add devcontainer support"
- User wants a sandboxed Claude Code development environment
- User needs isolated development environments with persistent configuration

## Do not use this skill when

- User already has a devcontainer configuration and just needs modifications
- User is asking about general Docker or container questions
- User wants to deploy production containers (this is for development only)

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
- Phase 1: Project Reconnaissance
- Phase 2: Generate Configuration
- Base Template Features
- Language-Specific Sections
- Reference Material
- Adding Persistent Volumes
- Output Files
- Validation Checklist
- User Instructions

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring... | First. Always. |
| `references/dockerfile-best-practices.md` | Dockerfile Best Practices: Choose minimal, trusted base images: | When a step points to it, or when you need the detail. |
| `references/features-vs-dockerfile.md` | Features vs Dockerfile: For Python, we use Dockerfile + uv instead of the Python feature because: | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/devcontainer-setup/skills/devcontainer-setup/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
