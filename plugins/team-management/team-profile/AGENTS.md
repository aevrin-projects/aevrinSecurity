# Agent guide: team-profile plugin

Category: Team Management
Folder: plugins/team-management/team-profile/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Interprets Team Profile survey results for individuals and teams

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| interpreting-team-profile | Interprets Team Profile (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout... | `skills/interpreting-team-profile/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Team Profile: Interprets Team Profile survey results for individuals and teams. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
