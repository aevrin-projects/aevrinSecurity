# Agent guide: dwarf-debug-info plugin

Category: Reverse Engineering
Folder: plugins/reverse-engineering/dwarf-debug-info/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Analyze DWARF debug information: parse and search DIEs with dwarfdump and readelf, verify debug info integrity, and write DWARF parsing code

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| dwarf-debug-info | Analyzes DWARF debug information in compiled binaries. Use when inspecting .debug_* sections, DIE trees, or DW_TAG_/DW_AT_ entries with dwarfdump/llvm-dwarfdump or readelf, verifying debug info... | `skills/dwarf-debug-info/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | DWARF Expert: Interact with and analyze DWARF debug information: parse and search DIEs with | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
