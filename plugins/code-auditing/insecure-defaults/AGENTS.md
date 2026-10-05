# Agent guide: insecure-defaults plugin

Category: Code Auditing
Folder: plugins/code-auditing/insecure-defaults/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Detects insecure default configurations including hardcoded credentials, fallback secrets, weak authentication defaults, and dangerous values in production

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `commands/audit.md` | Audit a file, directory, or whole repo for insecure default configuration: fallback secrets, default credentials, fail-open switches, weak crypto, permissive access, debug leakage. Parallel sweeps collect candidates, then a... | Saved prompt. Say: "Follow plugins/code-auditing/insecure-defaults/commands/audit.md on the target." |
| `README.md` | Insecure Defaults Detection: Audits a codebase for insecure default configuration, tracing each candidate before reporting it. | Human documentation. Read it for install notes and extra details. |
| `references/debug-features.md` | Debug and Introspection Defaults: Report when: Internal detail reaches a response, a listening port, or a log a lower-privileged party can read, whether it is gated by a flag that defaults to on, or simply unconditional (a... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/debug-features.md before you start." |
| `references/default-credentials.md` | Default Credentials: Report when: A credential literal that a running deployment can actually authenticate with, including seeded accounts created on first boot. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/default-credentials.md before you start." |
| `references/fail-open-security.md` | Fail-Open Security Switches: Report when: The value taken when configuration is absent disables a security control. The insecure state is the unconfigured state. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/fail-open-security.md before you start." |
| `references/fallback-secrets.md` | Fallback Secrets: Report when: A default value supplied when the env var is absent, where that value feeds signing, encryption, session, or token machinery. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/fallback-secrets.md before you start." |
| `references/permissive-access.md` | Permissive Access Defaults: Report when: Access is granted to a party who should not have it, either because that is the hardcoded value (ACL='public-read', mode 0o666, Access-Control-Allow-Origin '*') or because it is what... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/permissive-access.md before you start." |
| `references/weak-crypto.md` | Weak Cryptographic Defaults: Report when: A broken or non-cryptographic primitive standing in for a security-relevant one: password hashing, token generation, encryption, signature verification. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/weak-crypto.md before you start." |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
