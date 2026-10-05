# Security Audit

The flagship Aevrin Security skill. It runs a structured, source-first security audit of a codebase and writes validated findings and reports.

The skill files are in `skills/security-audit/`. This skill is agent-neutral. Any coding agent that can read files, run shell commands, and (optionally) start sub-agents can follow it. Start with `skills/security-audit/SKILL.md`.

## What it does

The skill runs a structured audit in six phases:

1. **Reconnaissance** -- map architecture, trust boundaries, input surfaces, prior evidence, and deterministic coverage in `architecture.md` and `coverage-ledger.json`.
2. **Coverage-led hunting** -- assign isolated hunters from ledger units, record their checks, and use coverage critics to find gaps.
3. **Candidate validation** -- give every unique candidate to a fresh verifier that tries to disprove it.
4. **Structured output** -- write `confirmed`, `needs_validation`, and `rejected` records to `findings.json` and validate them against `report-schema.json`.
5. **Independent record verification** -- fresh agents verify final source claims. Material replacements receive another independent verifier.
6. **Target-neutral reporting** -- derive `REPORT.md`, `FINDINGS-DETAIL.md`, and `NEEDS-VALIDATION.md` from the verified records and coverage ledger.

The parent runs `validate-coverage-ledger.cjs` after creating the ledger and after each later ledger update. It runs `validate-findings.cjs` in Phase 4 and again after every Phase 5 replacement.

The verdicts are distinct: `confirmed` has a complete source trace and bounded observed result, `needs_validation` has an exact unresolved fact and no severity, and `rejected` records a disproved candidate.

Multiple runs against the same repo are additive. The skill uses prior ledgers and findings to target gaps, revalidate changed source, and carry forward current-source evidence without treating stale or unresolved work as covered.

## Files

| File | Purpose |
|------|---------|
| `skills/security-audit/SKILL.md` | Setup, core principles, platform terminology, workflow overview, and audit anti-patterns |
| `skills/security-audit/RECONNAISSANCE.md` | Phase 1 reconnaissance prompts and synthesis instructions |
| `skills/security-audit/HUNTING.md` | Phase 2 orchestration, hunting methodology, and validation rules |
| `skills/security-audit/ATTACK-CLASSES.md` | Core, wildcard, and obvious-things attack prompts |
| `skills/security-audit/MEMORY-SAFETY-AND-BINARY.md` | Memory-safety, binary, and kernel hunting classes for native targets |
| `skills/security-audit/AI-AND-LLM.md` | Prompt-injection, agent/tool, and output-handling hunting classes for LLM-backed targets |
| `skills/security-audit/WEB-PROTOCOL-AND-AUTH.md` | HTTP request-framing, cache, and authentication-protocol hunting classes for HTTP-protocol and auth targets |
| `skills/security-audit/CLIENT-SIDE.md` | DOM-injection, messaging-trust, UI-redress, and prototype-pollution hunting classes for client-side/browser targets |
| `skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md` | Dependency, CI, release, signing, update, plugin, and extension hunting classes |
| `skills/security-audit/CLOUD-AND-DEPLOYMENT.md` | IAM, infrastructure-as-code, container, serverless, ingress, and runtime-configuration hunting classes |
| `skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md` | RPC, serialization, queue, broker, webhook, and streaming-protocol hunting classes |
| `skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md` | Shared resource, quota, queue, worker, and operator-spend hunting classes |
| `skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md` | Tenant isolation, cache, search, export, backup, migration, deletion, and restore hunting classes |
| `skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md` | Native app, deep-link, webview, exported-component, helper, daemon, and local-IPC hunting classes |
| `skills/security-audit/VALIDATION-AND-REPORTING.md` | Phases 3-6 candidate validation, structured output, record verification, and reporting |
| `skills/security-audit/report-schema.json` | JSON schema for all three `findings.json` verdicts |
| `skills/security-audit/validate-findings.cjs` | Zero-dependency validator for `findings.json` in Phases 4 and 5 |
| `skills/security-audit/validate-findings.test.cjs` | Findings-validator tests and producer-compatible fixture checks |
| `skills/security-audit/validate-coverage-ledger.cjs` | Zero-dependency validator for `coverage-ledger.json` in Phases 1-5 |
| `skills/security-audit/validate-coverage-ledger.test.cjs` | Coverage-ledger validator tests |

## Usage

Start your coding agent in (or pointed at) the codebase you want to audit, then ask it to do a security audit:

```
security audit this codebase
```

```
find security vulnerabilities in ./src
```

```
do a security review, output to ~/audits/my-project
```

The skill activates automatically when the request matches its trigger (security audit, find vulnerabilities, pen-test the code, etc.). A direct codebase audit or pen-test request uses full audit mode. Security questions and focused vulnerability work use guidance mode unless you request report artifacts. In full audit mode, an unspecified output directory defaults to `~/security-audit-skill/<repo-name>/run-<N>`. The workflow writes inside the target repository only when you explicitly select a directory that version control ignores.

## Requirements

- A coding agent with a model that supports tool use and parallel sub-agents
- Node.js for the zero-dependency findings and coverage-ledger validators
- An OS-enforced sandbox for target-controlled builds, tests, processes, browsers, emulators, fuzzers, and fixtures. It must disable external networking, use a sanitized allowlisted environment, enforce resource limits, and allow writes only to assigned scratch paths. Without these controls, the workflow keeps the lead as `needs_validation` instead of executing target code.

## Design principles

- **Only confirm established boundary failures.** Keep a source-grounded blocked lead as `needs_validation` with its exact unresolved fact.
- **Adversarial validation.** The agent that checks a finding is never the agent that found it.
- **Severity requires impact.** Likelihood x impact, not deviation from a checklist.
- **Defense-in-depth gaps are not vulnerabilities.** If Layer A prevents the attack, the absence of Layer B is a hardening note.
- **Multiple runs improve coverage.** In test runs, a single run found roughly half of the vulnerabilities that repeated runs found in total.