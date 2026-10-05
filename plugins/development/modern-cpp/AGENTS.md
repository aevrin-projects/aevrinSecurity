# Agent guide: modern-cpp plugin

Category: Development
Folder: plugins/development/modern-cpp/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Modern C++ best practices (C++20/23/26). Use when writing C++ code, creating new C++ projects, or modernizing legacy C++ patterns.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| modern-cpp | Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces raw pointers with smart pointers,... | `skills/modern-cpp/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | modern-cpp: Modern C++ best practices plugin for coding agents, guiding AI-assisted development toward C++20/23/26 idioms with a security emphasis from Aevrin Security. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
