# Agent guide: post-patch-validation plugin

Category: Verification
Folder: plugins/verification/post-patch-validation/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Validates security patches against the reported bug, root-cause variants, and surrounding behavior. Returns reproducible failures to repair and validation gaps, with pinned inputs and saved evidence. Bundles a validate-patch dynamic workflow for Claude Code.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| post-patch-validation | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security... | `skills/post-patch-validation/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Post-Patch Validation: Validate a security patch against the reported bug and the surrounding code it affects. Give the | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
