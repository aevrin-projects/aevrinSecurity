# Agent guide: firebase-apk-scanner plugin

Category: Mobile Security
Folder: plugins/mobile-security/firebase-apk-scanner/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Scan Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. For authorized security research only.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| firebase-apk-scanner | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase... | `skills/firebase-apk-scanner/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/scan-apk.md` | Scans Android APKs for Firebase security misconfigurations | Saved prompt. Say: "Follow plugins/mobile-security/firebase-apk-scanner/commands/scan-apk.md on the target." |
| `README.md` | Firebase APK Security Scanner: Scan Android APKs for Firebase security misconfigurations including open databases, exposed storage buckets, and authentication bypasses. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
