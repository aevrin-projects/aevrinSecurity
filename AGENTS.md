# Guide for coding agents

This repository holds security skills from Aevrin Security. Use this file if you are an AI coding agent working with these skills.

## Where to start

- Read [README.md](README.md) for the folder layout.
- Read [catalog.json](catalog.json) to find a skill by name, category, or description.
- Read [USAGE.md](USAGE.md) to see how users ask for each skill.
- Each plugin and skill folder has its own `AGENTS.md` with a map of every file in it. Read it before you load other files.
- Open the skill's `SKILL.md`. That file is the entry point. Follow it in order.
- Load other files in the skill folder (references, workflows, templates) only when `SKILL.md` tells you to.

## Rules

- Do the work the skill describes. Do not skip phases or checks.
- Skill paths such as `{baseDir}` mean the folder that holds the `SKILL.md` you are reading.
- Write results where the skill says. Do not write inside the target project unless the user agreed.
- Do not run code from the target project outside a sandbox.
- If a feature below is not available to you, use the fallback in the table.

## Agent-neutral terms

Some skills were written with tool names from one product. Read them with this table.

| Term in a skill | What it means | Fallback if you do not have it |
|---|---|---|
| Task tool, subagent, Agent | Start a separate worker with its own context and give it a prompt | Do the work yourself, one step at a time, in a fresh section of your notes |
| Parallel workers | Run several workers at the same time | Run them one after the other |
| AskUserQuestion | Ask the user a question and wait | Ask in plain chat and wait for the answer |
| TaskCreate, TaskUpdate, TodoWrite | Keep a checklist of steps | Keep a checklist in a Markdown file or in your notes |
| WebFetch | Download and read a web page | Use curl or any fetch tool you have |
| Read, Grep, Glob, Edit, Write, Bash | Read files, search text, find files, edit files, write files, run shell commands | Use your own file and shell tools |
| `allowed-tools` (front matter) | A list of tools the skill expects | Ignore it. It is a hint only |
| `${CLAUDE_PLUGIN_ROOT}` | The plugin folder, for example `plugins/code-auditing/risky-apis` | Replace it with the real path before you run a command |
| `{baseDir}` | The skill folder that holds `SKILL.md` | Replace it with the real path |
| `CLAUDE.md` | A file of project notes for an agent | Use `AGENTS.md` or your own notes file |
| Slash command such as `/name` | A saved prompt in a `commands/` folder | Open the matching file in `commands/` and follow it |
| `agents/*.md` | Prompts for sub-agents | Use the text as the prompt for a worker, or follow it yourself |
| `agents/openai.yaml` | Display name and short text for tools that show skill lists | Ignore it |
| `hooks/` | Automation that runs at set moments | Optional. Ignore it, or copy the checks into your own setup |
| `workflows/*.js` | Scripts that run many steps | Follow the matching steps in `SKILL.md` by hand |

## Plugin folder rules

- `plugin.json` has the name, description, and author. It has no version.
- Each plugin keeps its own README with its details.
- Tests and evals are for maintainers. You do not need them to use a skill.
