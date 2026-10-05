# Agent guide: modern-python

Plugin: modern-python (Development)
Skill folder: plugins/development/modern-python/skills/modern-python/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black.

## Use this skill when

- Creating a new Python project or package
- Setting up `pyproject.toml` configuration
- Configuring development tools (linting, formatting, testing)
- Writing Python scripts with external dependencies
- Migrating from legacy tools (when user requests it)

## Do not use this skill when

- **User wants to keep legacy tooling**: Respect existing workflows if explicitly requested
- **Python < 3.11 required**: These tools target modern Python
- **Non-Python projects**: Mixed codebases where Python isn't primary

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
- Tool Overview
- Quick Start: Minimal Project
- Full Project Setup
- Migration Guide
- Quick Reference: uv Commands
- Quick Reference: Dependency Groups
- Best Practices Checklist
- Read Next

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. | First. Always. |
| `references/dependabot.md` | Dependabot: Automated Dependency Updates: [Dependabot](https://docs.github.com/en/code-security/dependabot) automatically creates pull requests to keep your dependencies up to date. GitHub hosts it natively-no external service... | When a step points to it, or when you need the detail. |
| `references/migration-checklist.md` | Migration Checklist: Comprehensive checklist for migrating Python projects to modern tooling. | When a step points to it, or when you need the detail. |
| `references/pep723-scripts.md` | PEP 723: Inline Script Metadata: PEP 723 allows embedding dependency metadata directly in Python scripts, eliminating the need for separate requirements.txt or pyproject.toml files for simple scripts. | When a step points to it, or when you need the detail. |
| `references/prek.md` | prek: Fast Pre-commit Hooks: [prek](https://github.com/j178/prek) is a fast, Rust-native drop-in replacement for pre-commit. It uses the same .pre-commit-config.yaml format and is fully compatible with existing configurations. | When a step points to it, or when you need the detail. |
| `references/pyproject.md` | pyproject.toml Configuration Reference: Complete reference for configuring pyproject.toml for modern Python projects. | When a step points to it, or when you need the detail. |
| `references/ruff-config.md` | Ruff Configuration Reference: Ruff is an extremely fast Python linter and formatter written in Rust. It replaces flake8, black, isort, pyupgrade, pydocstyle, and many other tools. | When a step points to it, or when you need the detail. |
| `references/security-setup.md` | Security Setup: Security tooling for Python projects: pre-commit hooks, CI auditing, and dependency scanning. | When a step points to it, or when you need the detail. |
| `references/testing.md` | Testing with pytest: Configuration and best practices for pytest with coverage enforcement. | When a step points to it, or when you need the detail. |
| `references/uv-commands.md` | uv Command Reference: uv is an extremely fast Python package and project manager written in Rust. It replaces pip, virtualenv, pip-tools, pipx, and pyenv. | When a step points to it, or when you need the detail. |

## Example requests

- Use: Use plugins/development/modern-python/skills/modern-python/SKILL.md. Task: <describe what you want>. Target: this repository.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
