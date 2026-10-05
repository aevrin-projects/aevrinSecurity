# Agent guide: agentic-actions-auditor

Plugin: agentic-actions-auditor (Code Auditing)
Skill folder: plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

## Use this skill when

- Auditing a repository's GitHub Actions workflows for AI agent security
- Reviewing CI/CD configurations that invoke Claude Code Action, Gemini CLI, or OpenAI Codex
- Checking whether attacker-controlled input can reach AI agent prompts
- Evaluating agentic action configurations (sandbox settings, tool permissions, user allowlists)
- Assessing trigger events that expose workflows to external input (`pull_request_target`, `issue_comment`, etc.)
- Investigating data flow from GitHub event context through `env:` blocks to AI prompt fields

## Do not use this skill when

- Analyzing workflows that do NOT use any AI agent actions (use general Actions security tools instead)
- Reviewing standalone composite actions or reusable workflows outside of a caller workflow context (use this skill when analyzing a workflow that references them via `uses:`)
- Performing runtime prompt injection testing (this is static analysis guidance, not exploitation)
- Auditing non-GitHub CI/CD systems (Jenkins, GitLab CI, CircleCI)
- Auto-fixing or modifying workflow files (this skill reports findings, does not modify files)

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- When to Use
- When NOT to Use
- Rationalizations to Reject
- Audit Methodology
- Detailed References

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input... | First. Always. |
| `references/action-profiles.md` | Action Security Profiles: Security-relevant configuration fields, default behaviors, dangerous configuration patterns, and remediation guidance for each supported AI action. Referenced by SKILL.md Step 5 for action-specific... | When a step points to it, or when you need the detail. |
| `references/cross-file-resolution.md` | Cross-File Resolution: Composite Actions and Reusable Workflows: AI agents can be hidden inside composite actions and reusable workflows, invisible when analyzing only the caller workflow file. This reference documents how to... | When a step points to it, or when you need the detail. |
| `references/foundations.md` | Shared Foundations: Attacker-Controlled Input Model: This reference documents cross-cutting concepts that all 9 attack vector detection heuristics depend on. Read this before analyzing individual vectors. | When a step points to it, or when you need the detail. |
| `references/vector-a-env-var-intermediary.md` | Vector A: Env Var Intermediary: Attacker data flows from GitHub event context into env: blocks, and the AI prompt references those env var names -- the AI agent reads the attacker content from environment variables at runtime.... | When a step points to it, or when you need the detail. |
| `references/vector-b-direct-expression-injection.md` | Vector B: Direct Expression Injection: Direct ${{ github.event.* }} expressions embedded in AI prompt fields. The YAML engine evaluates the expression at workflow runtime, embedding the attacker's raw text directly into the... | When a step points to it, or when you need the detail. |
| `references/vector-c-cli-data-fetch.md` | Vector C: CLI Data Fetch: The prompt instructs the AI agent to fetch attacker-controlled content at runtime using gh CLI commands. The prompt itself may contain no dangerous expressions or env vars with attacker data, but the... | When a step points to it, or when you need the detail. |
| `references/vector-d-pr-target-checkout.md` | Vector D: pull_request_target + PR Head Checkout: An attacker opens a fork pull request against a repository that uses pull_request_target to trigger an AI agent workflow. Because pull_request_target runs the workflow... | When a step points to it, or when you need the detail. |
| `references/vector-e-error-log-injection.md` | Vector E: Error Log Injection: CI error output, build logs, or test failure messages are fed to an AI agent as context. An attacker crafts code that produces prompt injection payloads in compiler errors, test failure output,... | When a step points to it, or when you need the detail. |
| `references/vector-f-subshell-expansion.md` | Vector F: Subshell Expansion in Restricted Tool Lists: Tool restriction lists include commands that support subshell expansion (e.g., echo), allowing echo $(env) or echo $(whoami) to bypass the restriction and execute... | When a step points to it, or when you need the detail. |
| `references/vector-g-eval-of-ai-output.md` | Vector G: Eval of AI Output: AI agent response is consumed by a subsequent workflow step that passes it through eval, exec, shell expansion, or other code execution sinks. If an attacker can influence the AI's output (via any... | When a step points to it, or when you need the detail. |
| `references/vector-h-dangerous-sandbox-configs.md` | Vector H: Dangerous Sandbox Configurations: AI action sandbox or safety configurations are set to values that disable protections entirely, giving the AI agent unrestricted shell access, filesystem access, or approval-free... | When a step points to it, or when you need the detail. |
| `references/vector-i-wildcard-allowlists.md` | Vector I: Wildcard User Allowlists: User allowlist fields are set to wildcard values ("*") that permit ANY GitHub user -- including external contributors, anonymous users, and potential attackers -- to trigger the AI agent.... | When a step points to it, or when you need the detail. |

## Example requests

- Find: Use plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md. Scan the GitHub Actions workflows in .github/workflows. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md. Scan the GitHub Actions workflows in .github/workflows. Write a detailed report to ./reports/agentic-actions-auditor.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/agentic-actions-auditor.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
