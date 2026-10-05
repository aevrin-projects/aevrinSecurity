# Agent guide: random-pick plugin

Category: Development
Folder: plugins/development/random-pick/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Draws the 12 Houses of the Zodiac Tarot spread using cryptographic randomness to add 100+ bits of entropy to vague or underspecified planning. Interprets the spread to guide next steps. Use when feeling lucky, invoking heart-of-the-cards energy, or when prompts are ambiguous.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| random-pick | Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the... | `skills/random-pick/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/draw.md` | Draw the 12 Houses of the Zodiac Tarot spread and return a concise structured reading. Use as a named agent instead of wrapping Skill(random-pick) in an Agent call. Callers get just the verdict text; card file content stays in... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/development/random-pick/agents/draw.md." |
| `README.md` | random-pick: A Claude Code skill that draws Tarot cards using secrets to inject | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
