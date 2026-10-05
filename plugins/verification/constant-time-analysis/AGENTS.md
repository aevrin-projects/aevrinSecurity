# Agent guide: constant-time-analysis plugin

Category: Verification
Folder: plugins/verification/constant-time-analysis/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Detect compiler-induced timing side-channels in cryptographic code

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| constant-time-analysis | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time... | `skills/constant-time-analysis/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/ct-check.md` | Detects timing side-channels in cryptographic code | Saved prompt. Say: "Follow plugins/verification/constant-time-analysis/commands/ct-check.md on the target." |
| `README.md` | Constant-Time Analyzer (ct-analyzer): A portable tool for detecting timing side-channel vulnerabilities in compiled cryptographic code. Analyzes assembly output from multiple compilers and architectures to detect instructions... | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
