# Agent guide: burpsuite-project-parser plugin

Category: Code Auditing
Folder: plugins/code-auditing/burpsuite-project-parser/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Search and extract data from Burp Suite project files (.burp) for security analysis

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| burpsuite-project-parser | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy... | `skills/burpsuite-project-parser/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/burp-search.md` | Searches Burp Suite project files for security analysis | Saved prompt. Say: "Follow plugins/code-auditing/burpsuite-project-parser/commands/burp-search.md on the target." |
| `README.md` | Burp Suite Project Parser: Search and extract data from Burp Suite project files (.burp) for use in Claude | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
