# Agent guide: git-cleanup plugin

Category: Development
Folder: plugins/development/git-cleanup/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/git-cleanup.md` | Safely analyzes and cleans up local git branches and worktrees, categorizing them as merged, squash-merged, superseded, or active work before deleting anything. | Saved prompt. Say: "Follow plugins/development/git-cleanup/commands/git-cleanup.md on the target." |
| `README.md` | git-cleanup: An agent command for safely cleaning up accumulated git worktrees and local branches. | Human documentation. Read it for install notes and extra details. |
| `references/merge-evidence.md` | Merge Evidence Standard: What counts as proof that a branch's work is already in the default branch, and what does not. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/git-cleanup/references/merge-evidence.md before you start." |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
