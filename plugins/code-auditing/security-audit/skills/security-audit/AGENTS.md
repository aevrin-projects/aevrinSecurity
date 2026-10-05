# Agent guide: security-audit

Plugin: security-audit (Code Auditing)
Skill folder: plugins/code-auditing/security-audit/skills/security-audit/

This file tells a coding agent how to work in this skill folder. For general rules and the agent-neutral term table, read the root AGENTS.md first. For user-facing examples, see USAGE.md.

## Purpose

Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete workflow only for explicit codebase audit or pen-test requests, full/comprehensive/end-to-end reviews, or requested report artifacts.

## How to start

1. Open `SKILL.md` in this folder and read it fully before you act.
2. Follow its steps in order. Do not skip steps or checks.
3. Load a file from the table below only when `SKILL.md` or a loaded file points to it.
4. Write results where `SKILL.md` says. If it does not say, write to `./reports/` and tell the user the path.
5. Do not change the target code unless the user asked for a fix.

## Outline of SKILL.md

- Operating modes
- Platform terminology
- Universal execution safety
- Full audit setup
- Full audit planning
- Core principles
- Full audit workflow
- Anti-patterns

## Files in this folder

| File | What it is | When to load it |
|---|---|---|
| `SKILL.md` | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete... | First. Always. |
| `AI-AND-LLM.md` | AI, LLM, and Agent Hunting: Reach for this file when a language model participates in a trust-sensitive decision: chatbots and assistants, RAG pipelines, persistent agent memory, agent/tool-calling loops, MCP servers and... | When a step points to it. |
| `ATTACK-CLASSES.md` | Attack Classes: Select attack classes relevant to the application type. Not every class applies to every codebase. The list below is a starting point; add application-specific classes from Phase 1 and split large codebases per... | When a step points to it. |
| `CLIENT-SIDE.md` | Client-Side and Browser Hunting: Reach for this file when meaningful trust decisions or untrusted rendering happen in a browser: single-page apps, browser extensions, embedded webviews, service workers, offline applications,... | When a step points to it. |
| `CLOUD-AND-DEPLOYMENT.md` | Cloud and Deployment Hunting: Reach for this file when the repository defines cloud identity, infrastructure, containers, Kubernetes, service mesh, serverless functions, edge workers, ingress, object storage, managed services,... | When a step points to it. |
| `DATA-ISOLATION-AND-LIFECYCLE.md` | Data Isolation and Lifecycle Hunting: Reach for this file when the target stores multi-tenant or access-controlled data, derives search/index/cache/analytics copies, issues object links, exports or restores records, migrates... | When a step points to it. |
| `DESKTOP-MOBILE-AND-LOCAL-IPC.md` | Desktop, Mobile, and Local IPC Hunting: Reach for this file when the target is a desktop or mobile app, privileged helper, updater, local daemon, webview host, deep-link handler, browser native-messaging host, or local IPC... | When a step points to it. |
| `HUNTING.md` | Vulnerability Hunting: The parent assigns planned ledger units to general agents. Use enough focused hunters to cover the units without combining unrelated boundaries. One hunter may own closely related units in one subsystem;... | When a step points to it. |
| `MEMORY-SAFETY-AND-BINARY.md` | Memory Safety, Binary, and Kernel Hunting: Reach for this file when the target processes untrusted bytes in a memory-unsafe or privileged context: C/C++/Objective-C, Rust unsafe, FFI, kernel modules and drivers, parsers and... | When a step points to it. |
| `PROTOCOLS-RPC-AND-MESSAGING.md` | Protocols, RPC, and Messaging Hunting: Reach for this file when the target uses gRPC, GraphQL transports, Cap'n Proto, Thrift, Protobuf, custom binary protocols, streaming RPC, webhooks, brokers, queues, pub/sub, or event... | When a step points to it. |
| `RECONNAISSANCE.md` | Reconnaissance: The parent initializes run-metadata.json, applies the strict pre-reconnaissance budget gate in SKILL.md, then creates agent scratch roots and the shared ledger before hunting. If the gate fails, record the... | When a step points to it. |
| `RESOURCE-EXHAUSTION-AND-AVAILABILITY.md` | Resource Exhaustion and Availability Hunting: Reach for this file when untrusted requests, messages, files, tenant state, or agent work can consume CPU, memory, disk, connections, worker slots, paid APIs, or queue capacity, or... | When a step points to it. |
| `SUPPLY-CHAIN-AND-RELEASE.md` | Supply Chain and Release Hunting: Reach for this file when the target resolves dependencies, builds from untrusted contributions, runs CI, creates release artifacts, signs or promotes builds, loads plugins, or updates deployed... | When a step points to it. |
| `VALIDATION-AND-REPORTING.md` | Validation, Structured Output, Verification, and Reporting: After the clean coverage-critic pass or an explicitly recorded early stop, consolidate Phase 2 candidates and carried same-source prior confirmations by stable... | When a step points to it. |
| `WEB-PROTOCOL-AND-AUTH.md` | HTTP-Protocol and Authentication Hunting: Reach for this file when the target speaks HTTP at a parsing, caching, browser-authentication, or identity boundary: web applications, APIs, reverse proxies, CDNs, gateways, custom... | When a step points to it. |

## Example requests

- Find: Use plugins/code-auditing/security-audit/skills/security-audit/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.
- Report: Use plugins/code-auditing/security-audit/skills/security-audit/SKILL.md. Scan this repository. Write a detailed report to ./reports/security-audit.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.
- Fix: Read ./reports/security-audit.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.

## Rules for this skill

- Report only what you can show with evidence from the code or tool output.
- Say clearly when something is a guess or could not be checked.
- Keep each finding tied to a file and a line.
- Never run code from the target project outside a sandbox.
- If a step needs a tool you do not have, say so and use the fallback in the root AGENTS.md.
