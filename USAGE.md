# Usage guide

This guide shows how to use every skill and plugin in this repository with any coding agent. It lists what each skill does, the Markdown files inside it, and ready-to-copy requests for finding problems, writing reports, and fixing code.

## Contents

1. [How it works](#how-it-works)
2. [The three modes: find, report, fix](#the-three-modes-find-report-fix)
3. [Blockchain security walkthrough](#blockchain-security-walkthrough)
4. [Other common workflows](#other-common-workflows)
5. [Skill reference](#skill-reference)

## How it works

A skill is a folder. The file `SKILL.md` inside it holds the instructions. Other `.md` files in the folder are loaded only when the instructions need them.

You use a skill by telling your agent which file to read and what to do. The pattern is:

```
Use <path to SKILL.md>. <what to do>. <target>. <what to write and where>.
```

Example:

```
Use plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md. Scan ./programs. Write a detailed report to ./reports/solana.md.
```

Tips:

- Use the path from the repository root. If the repository is somewhere else, give the full path.
- If your agent can load skills from a folder, copy the skill there (see [README.md](README.md)) and just name the skill.
- Start with a small target (one program, one folder) and grow from there.
- Each skill folder has an `AGENTS.md` for the agent. It lists every file in that folder and when to load it.
- Open the report before you ask for fixes. You stay in control of what changes.

## The three modes: find, report, fix

Most security skills work in three steps. You can run one, two, or all three.

| Mode | What you ask | What the agent does | Does it change code? |
|---|---|---|---|
| Find | "List the vulnerabilities in X" | Reads the code, follows the skill, lists issues in chat | No |
| Report | "Write a detailed report to ./reports/name.md" | Does the same work and saves evidence, severity, and a suggested fix for each issue | No |
| Fix | "Read the report and fix the issues" | Edits code one issue at a time, highest severity first, and re-checks each fix | Yes |

Recommended order: **Find, then Report, then check the findings, then Fix, then validate the fix.** The "check the findings" step is done by the false-positive-check skill. The "validate the fix" step is done by post-patch-validation. Both are described below.

## Blockchain security walkthrough

Folders: `plugins/smart-contract-security/`, `plugins/code-auditing/`, `plugins/verification/`

Say you have a Solana program in `./programs` and you want to find bugs, get a full report, and then fix them.

**Step 1. Map the code.** Learn what the contracts do before you hunt.

```
Use plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md. Read ./programs one function at a time and save your notes to ./reports/context.md.
```

**Step 2. List the entry points.** These are the functions an attacker can call.

```
Use plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md. List every state-changing entry point in ./programs and write it to ./reports/entry-points.md.
```

**Step 3. Find vulnerabilities.** Pick the scanner for your chain: algorand, cairo, cosmos, solana, substrate, or ton.

```
Use plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md. Scan ./programs and list every vulnerability with file, line, and impact. Do not change any code.
```

**Step 4. Write the detailed report.**

```
Use plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md. Scan ./programs. Write a detailed report to ./reports/solana.md. For each issue give severity, the exact code, how an attacker would use it, and a suggested fix. Do not change any code yet.
```

**Step 5. Remove false alarms.** Ask for a second look at each finding.

```
Use plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md. Check every finding in ./reports/solana.md. Give each one a TRUE POSITIVE or FALSE POSITIVE verdict with evidence. Update the report.
```

**Step 6. Fix.** Only after you have read the report.

```
Read ./reports/solana.md. Fix the confirmed issues one at a time, highest severity first. Add a test for each fix. Note each change in the report.
```

**Step 7. Check the fixes.** Make sure the patch did not miss a variant or break something.

```
Use plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md. Check the fixes I made for the issues in ./reports/solana.md. Look for missed variants and regressions.
```

Other skills you can add to this flow:

| Goal | Skill to name |
|---|---|
| Get a project ready for an outside audit | `plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md` |
| Score the maturity of a codebase | `plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md` |
| Review against development guidelines | `plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md` |
| Follow a secure development workflow | `plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md` |
| Check token integrations and ERC conformity | `plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md` |
| Find unit and formula mistakes | `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md` |
| Check code against its spec | `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md` |
| Write property tests and invariants (Echidna, Medusa) | `plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md` |
| Find weak tests with mutation testing | `plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md` |

## Other common workflows

**Full audit of any codebase** (web app, API, CLI, library)

```
Use plugins/code-auditing/security-audit/skills/security-audit/SKILL.md. Do a security audit of this repository. Write the output to ~/audits/my-project.
```

Then: false-positive-check on the findings, then ask the agent to fix the confirmed ones, then post-patch-validation.

**C or C++ project**

```
Use plugins/code-auditing/c-review/skills/c-review/SKILL.md. Review ./src and write a detailed report to ./reports/c-review.md.
```

**Rust project**

```
Use plugins/code-auditing/rust-review/skills/rust-review/SKILL.md. Review this crate and write a detailed report to ./reports/rust-review.md.
```

**Pull request or branch review**

```
Use plugins/code-auditing/differential-review/skills/differential-review/SKILL.md. Review the changes between main and this branch. Write a report to ./reports/diff-review.md.
```

**CI/CD with AI agents**

```
Use plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md. Audit .github/workflows and write a report.
```

**Android app**

```
Use plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md. Scan ./app.apk for Firebase misconfigurations and write a report.
```

**Dependencies**

```
Use plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md. Audit the dependencies of this project and write a report.
```

**Secrets left in memory (C, C++, Rust)**

```
Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md. Check that secrets in ./src are wiped from memory. Write a report.
```

**Is this bug real?**

```
Use plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md. Is this finding real? <paste finding>
```

**Write detection rules**

```
Use plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md. Write a Semgrep rule that finds <bug pattern>, with tests.
```

## Skill reference

Each section below covers one plugin: what it does, its skills, the requests you can copy, and every Markdown file in it with how to use that file.

### Smart Contract Security

#### building-secure-contracts

Folder: [plugins/smart-contract-security/building-secure-contracts/](plugins/smart-contract-security/building-secure-contracts/)  |  [README](plugins/smart-contract-security/building-secure-contracts/README.md)  |  [AGENTS.md](plugins/smart-contract-security/building-secure-contracts/AGENTS.md)

Comprehensive smart contract security toolkit based on the Building Secure Contracts framework. Includes vulnerability scanners for 6 blockchains and 5 development guideline assistants.

##### Skill: algorand-vulnerability-scanner

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md`

Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal).

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md. Scan the Algorand contracts in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md. Scan the Algorand contracts in this repository. Write a detailed report to ./reports/algorand-vulnerability-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/algorand-vulnerability-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md` | Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand projects (TEAL/PyTeal). | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md on the Algorand contracts in this repository." |
| `plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md` | VULNERABLE: No RekeyTo check: Description: Missing validation of the RekeyTo transaction field allows attackers to change account authorization and bypass contract restrictions. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/algorand-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md before you start." |

##### Skill: audit-prep-assistant

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md`

Prepares codebases for security review using Aevrin Security's checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation (flowcharts, user stories, inline comments). Use when preparing your own codebase to be audited by someone else, getting a repository review-ready before an external security review, deciding what to fix before auditors start, or asking what assessors need from a project. For understanding unfamiliar code you are about to audit, use code-understanding instead.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/audit-prep-assistant.md with ratings, evidence, and recommended changes.`
- **Fix:** `Read ./reports/audit-prep-assistant.md. Apply the recommended changes one at a time, then check each one.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md` | Prepares codebases for security review using Aevrin Security's checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and generates documentation... | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/audit-prep-assistant/SKILL.md on the smart contracts in ./contracts." |

##### Skill: cairo-vulnerability-scanner

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md`

Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md. Scan the Cairo contracts in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md. Scan the Cairo contracts in this repository. Write a detailed report to ./reports/cairo-vulnerability-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/cairo-vulnerability-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md` | Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing StarkNet projects. | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md on the Cairo contracts in this repository." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md` | Description: The felt252 type in Cairo represents field elements in range [0, P] where P is the StarkNet prime. Unchecked arithmetic can overflow (wrapping to 0) or underflow (wrapping to P-1), similar to unsigned intege | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cairo-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md before you start." |

##### Skill: code-maturity-assessor

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md`

Systematic code maturity assessment using Aevrin Security's 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level code, and testing, then produces a scorecard with evidence-based ratings and a priority-ordered roadmap. Use when assessing or scoring the maturity of a smart contract or blockchain codebase, producing a maturity scorecard or evaluation, or judging how mature, well-tested, or well-documented such a project is against a rubric.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/code-maturity-assessor.md with ratings, evidence, and recommended changes.`
- **Fix:** `Read ./reports/code-maturity-assessor.md. Apply the recommended changes one at a time, then check each one.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md` | Systematic code maturity assessment using Aevrin Security's 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization, documentation, MEV risks, low-level... | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/SKILL.md on the smart contracts in ./contracts." |
| `plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/resources/ASSESSMENT_CRITERIA.md` | Focus: Overflow protection, precision handling, formula specification, edge case testing | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/resources/ASSESSMENT_CRITERIA.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/resources/EXAMPLE_REPORT.md` | When the assessment is complete, you'll receive a comprehensive maturity report: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/resources/EXAMPLE_REPORT.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/resources/REPORT_FORMAT.md` | Overall: [X.X / 4.0] | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/code-maturity-assessor/resources/REPORT_FORMAT.md before you start." |

##### Skill: cosmos-vulnerability-scanner

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md`

Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities - chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/ modules, reviewing IBC integrations, or assessing pre-launch chain security. Updated for SDK v0.53.x.

Use it when:

- Auditing Cosmos SDK modules (custom `x/` modules)
- Reviewing CosmWasm smart contracts
- Pre-launch security assessment of Cosmos chains
- Investigating chain halt incidents

Do not use it when:

- Pure Solidity/EVM audits without Cosmos SDK - use Solidity-specific tools
- CometBFT consensus engine internals - this covers SDK modules, not the consensus layer itself
- General Go code review with no blockchain context
- Cosmos SDK application logic that is not consensus-critical (e.g., CLI commands, REST endpoints)
- CosmWasm contract-only audits on chains without custom SDK modules - use the CosmWasm checklist items alone

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md. Scan the Cosmos contracts in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md. Scan the Cosmos contracts in this repository. Write a detailed report to ./reports/cosmos-vulnerability-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/cosmos-vulnerability-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md` | Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities - chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when auditing custom x/... | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md on the Cosmos contracts in this repository." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/CHANGELOG.md` | Cosmos Vulnerability Scanner - Update Log: Added 8 missing vulnerability classes identified from real-world Cosmos findings catalog. Skill now covers 28 VULNERABILITY_PATTERNS + 16 IBC patterns. No existing patterns were... | Guide loaded during the work. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/CHANGELOG.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/ADVANCED_VULNERABILITY_PATTERNS.md` | Description: KV store key construction allows collisions, prefix overlaps, or unauthorized access to other users' data. Keys built via string concatenation without length-prefixed encoding create ambiguous boundaries. Nu | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/ADVANCED_VULNERABILITY_PATTERNS.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/COSMWASM_VULNERABILITY_PATTERNS.md` | Description: CosmWasm's Uint256, Uint512, Int256, and Int512 types used wrapping (modular) math for pow() and neg() instead of panicking on overflow. This means arithmetic silently wraps around on overflow, producing inc | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/COSMWASM_VULNERABILITY_PATTERNS.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/DISCOVERY.md` | Chain Audit Context: Explore the codebase and write a CLAUDE.md at the target repo root with all context needed for the audit. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/DISCOVERY.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/EVM_VULNERABILITY_PATTERNS.md` | Description: Precompiles bridge EVM and Cosmos state machines. When a Solidity revert, try/catch, or out-of-gas (OOG) occurs, EVM state rolls back automatically, but Cosmos keeper writes made during the precompile call p | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/EVM_VULNERABILITY_PATTERNS.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/IBC_VULNERABILITY_PATTERNS.md` | Description: An attacker can create a malicious chain and [spoof IBC message fields](https://github.com/evmos/evmos/security/advisories/GHSA-5jgq-x857-p8xw). The counterparty chain controls the sender, memo, and other pa | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/IBC_VULNERABILITY_PATTERNS.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/STATE_VULNERABILITY_PATTERNS.md` | Description: Custom internal accounting alongside x/bank module becomes inconsistent when direct token transfers bypass internal bookkeeping. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/STATE_VULNERABILITY_PATTERNS.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md` | .golangci.yml: Description: Non-deterministic code in consensus causes different validators to produce different state roots, halting the chain. This is the most severe Cosmos vulnerability. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/cosmos-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md before you start." |

##### Skill: guidelines-advisor

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md`

Smart contract development advisor based on Aevrin Security's best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality, identify pitfalls, review dependencies, and evaluate testing. Use when asking whether a smart contract project follows development best practices, reviewing on-chain/off-chain split, upgradeability, or delegatecall proxy patterns against guidelines, or seeking recommendations on contract design, inheritance, events, documentation, dependencies, or test strategy.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/guidelines-advisor.md with ratings, evidence, and recommended changes.`
- **Fix:** `Read ./reports/guidelines-advisor.md. Apply the recommended changes one at a time, then check each one.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md` | Smart contract development advisor based on Aevrin Security's best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess implementation quality,... | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/SKILL.md on the smart contracts in ./contracts." |
| `plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/resources/ASSESSMENT_AREAS.md` | What I'll do: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/resources/ASSESSMENT_AREAS.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/resources/DELIVERABLES.md` | Plain English Description: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/resources/DELIVERABLES.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/resources/EXAMPLE_REPORT.md` | When the analysis is complete, you'll receive comprehensive guidance like this: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/guidelines-advisor/resources/EXAMPLE_REPORT.md before you start." |

##### Skill: secure-workflow-guide

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md`

Guides through Aevrin Security's 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security properties for fuzzing/verification, and reviews manual security areas. Use when securing a smart contract end to end rather than hunting one bug, checking a project on every check-in or before deployment, triaging a Slither report, or asking where to start on smart contract security.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/secure-workflow-guide.md with ratings, evidence, and recommended changes.`
- **Fix:** `Read ./reports/secure-workflow-guide.md. Apply the recommended changes one at a time, then check each one.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md` | Guides through Aevrin Security's 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, helps document security... | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/SKILL.md on the smart contracts in ./contracts." |
| `plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/resources/EXAMPLE_REPORT.md` | When I complete the workflow, you'll get a comprehensive security report: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/resources/EXAMPLE_REPORT.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/resources/WORKFLOW_STEPS.md` | I'll run Slither with 70+ built-in detectors: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/secure-workflow-guide/resources/WORKFLOW_STEPS.md before you start." |

##### Skill: solana-vulnerability-scanner

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md`

Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md. Scan the Solana contracts in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md. Scan the Solana contracts in this repository. Write a detailed report to ./reports/solana-vulnerability-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/solana-vulnerability-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md` | Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs. | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md on the Solana contracts in this repository." |
| `plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md` | Description: Using invoke() or invoke_signed() with user-controlled program IDs allows attackers to call malicious programs instead of the intended program. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/solana-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md before you start." |

##### Skill: substrate-vulnerability-scanner

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md`

Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md. Scan the Substrate contracts in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md. Scan the Substrate contracts in this repository. Write a detailed report to ./reports/substrate-vulnerability-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/substrate-vulnerability-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md` | Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME pallets. | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md on the Substrate contracts in this repository." |
| `plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md` | Substrate Vulnerability Patterns (7 Patterns): This document contains detailed descriptions, detection patterns, and mitigations for 7 critical Substrate/FRAME vulnerabilities. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/substrate-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md before you start." |

##### Skill: token-integration-analyzer

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md`

Token integration and implementation analyzer based on Aevrin Security's token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract composition and owner privileges, performs on-chain scarcity analysis, and evaluates how protocols handle non-standard tokens. Use when integrating or accepting arbitrary ERC20/ERC721 tokens, auditing a token implementation for standards conformity, or assessing risk from weird tokens such as fee-on-transfer, rebasing, missing return values, or blocklists.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md on the smart contracts in ./contracts. List the gaps, risks, and weak spots you find. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md on the smart contracts in ./contracts. Write a detailed report to ./reports/token-integration-analyzer.md with ratings, evidence, and recommended changes.`
- **Fix:** `Read ./reports/token-integration-analyzer.md. Apply the recommended changes one at a time, then check each one.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md` | Token integration and implementation analyzer based on Aevrin Security's token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, assesses contract... | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/SKILL.md on the smart contracts in ./contracts." |
| `plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/resources/ASSESSMENT_CATEGORIES.md` | Assessment Categories Reference: This document contains detailed assessment criteria for token analysis. Each category includes what to check, analysis methods, and verification checklists. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/resources/ASSESSMENT_CATEGORIES.md before you start." |
| `plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/resources/REPORT_TEMPLATES.md` | Report Templates: This document contains report templates and deliverables formats for token integration analysis. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/token-integration-analyzer/resources/REPORT_TEMPLATES.md before you start." |

##### Skill: ton-vulnerability-scanner

Entry point: `plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md`

Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts.

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md. Scan the Ton contracts in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md. Scan the Ton contracts in this repository. Write a detailed report to ./reports/ton-vulnerability-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/ton-vulnerability-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md` | Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC contracts. | Start here. Say: "Follow plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md on the Ton contracts in this repository." |
| `plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md` | Description: FunC uses integers for boolean values (0 = false, -1 = true). The bitwise NOT operator ~ on non-standard boolean values (positive integers) produces unexpected results, causing logic errors. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/building-secure-contracts/skills/ton-vulnerability-scanner/resources/VULNERABILITY_PATTERNS.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/building-secure-contracts/README.md` | Building Secure Contracts: Comprehensive smart contract security toolkit based on Aevrin Security's [Building Secure Contracts](https://github.com/crytic/building-secure-contracts) framework. | Human documentation. Read it for install notes and extra details. |

#### entry-point-analyzer

Folder: [plugins/smart-contract-security/entry-point-analyzer/](plugins/smart-contract-security/entry-point-analyzer/)  |  [README](plugins/smart-contract-security/entry-point-analyzer/README.md)  |  [AGENTS.md](plugins/smart-contract-security/entry-point-analyzer/AGENTS.md)

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level, and generates structured audit reports.

##### Skill: entry-point-analyzer

Entry point: `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md`

Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted, contract-only), and generates structured audit reports. Excludes view/pure/read-only functions. Use when auditing smart contracts (Solidity, Vyper, Solana/Rust, Move, TON, CosmWasm) or when asked to find entry points, audit flows, external functions, access control patterns, or privileged operations.

Use it when:

- Starting a smart contract security audit to map the attack surface
- Asked to find entry points, external functions, or audit flows
- Analyzing access control patterns across a codebase
- Identifying privileged operations and role-restricted functions
- Building an understanding of which functions can modify contract state

Do not use it when:

- Vulnerability detection (use code-understanding or domain-specific-audits)
- Writing exploit POCs (use solidity-poc-builder)
- Code quality or gas optimization analysis
- Non-smart-contract codebases
- Analyzing read-only functions (this skill excludes them)

Requests you can copy:

- **Find:** `Use plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md. Scan the smart contracts in ./contracts. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md. Scan the smart contracts in ./contracts. Write a detailed report to ./reports/entry-point-analyzer.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/entry-point-analyzer.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md` | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, admin, role-restricted,... | Start here. Say: "Follow plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md on the smart contracts in ./contracts." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/cosmwasm.md` | CosmWasm Entry Point Detection: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/cosmwasm.md before you start." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/move-aptos.md` | Move Entry Point Detection (Aptos): In Move, public functions can be invoked from transaction scripts (Aptos) and typically modify state. In addition, all entry functions are entrypoints. Package-protected (public package) and... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/move-aptos.md before you start." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/move-sui.md` | Move Entry Point Detection (Sui): In Move, public functions can be invoked from programmable transaction blocks (Sui) or transaction scripts (Aptos) and typically modify state. In addition, private entry functions are... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/move-sui.md before you start." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/solana.md` | Solana Entry Point Detection: In Solana, most program instructions modify state. Exclude view-only patterns: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/solana.md before you start." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/solidity.md` | Solidity Entry Point Detection: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/solidity.md before you start." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/ton.md` | TON Entry Point Detection (FunC/Tact): Focus on message handlers that modify state. Exclude read-only patterns: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/ton.md before you start." |
| `plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/vyper.md` | Vyper Entry Point Detection: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/smart-contract-security/entry-point-analyzer/skills/entry-point-analyzer/references/vyper.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/smart-contract-security/entry-point-analyzer/commands/entry-points.md` | Identifies state-changing entry points in smart contracts | Saved prompt. Say: "Follow plugins/smart-contract-security/entry-point-analyzer/commands/entry-points.md on the smart contracts in ./contracts." |
| `plugins/smart-contract-security/entry-point-analyzer/README.md` | Entry Point Analyzer: An agent skill for systematically identifying state-changing entry points in smart contract codebases to guide security audits. | Human documentation. Read it for install notes and extra details. |

### Code Auditing

#### security-audit

Folder: [plugins/code-auditing/security-audit/](plugins/code-auditing/security-audit/)  |  [README](plugins/code-auditing/security-audit/README.md)  |  [AGENTS.md](plugins/code-auditing/security-audit/AGENTS.md)

Source-first security audit workflow: reconnaissance, coverage-led hunting, adversarial validation, structured findings, and reports.

##### Skill: security-audit

Entry point: `plugins/code-auditing/security-audit/skills/security-audit/SKILL.md`

Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete workflow only for explicit codebase audit or pen-test requests, full/comprehensive/end-to-end reviews, or requested report artifacts.

Requests you can copy:

- **Find:** `Use plugins/code-auditing/security-audit/skills/security-audit/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/security-audit/skills/security-audit/SKILL.md. Scan this repository. Write a detailed report to ./reports/security-audit.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/security-audit.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/security-audit/skills/security-audit/SKILL.md` | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulnerability research, security audits, or pen tests. Run the complete... | Start here. Say: "Follow plugins/code-auditing/security-audit/skills/security-audit/SKILL.md on this repository." |
| `plugins/code-auditing/security-audit/skills/security-audit/AI-AND-LLM.md` | AI, LLM, and Agent Hunting: Reach for this file when a language model participates in a trust-sensitive decision: chatbots and assistants, RAG pipelines, persistent agent memory, agent/tool-calling loops, MCP servers and... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/AI-AND-LLM.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/ATTACK-CLASSES.md` | Attack Classes: Select attack classes relevant to the application type. Not every class applies to every codebase. The list below is a starting point; add application-specific classes from Phase 1 and split large codebases per... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/ATTACK-CLASSES.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/CLIENT-SIDE.md` | Client-Side and Browser Hunting: Reach for this file when meaningful trust decisions or untrusted rendering happen in a browser: single-page apps, browser extensions, embedded webviews, service workers, offline applications,... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/CLIENT-SIDE.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/CLOUD-AND-DEPLOYMENT.md` | Cloud and Deployment Hunting: Reach for this file when the repository defines cloud identity, infrastructure, containers, Kubernetes, service mesh, serverless functions, edge workers, ingress, object storage, managed services,... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/CLOUD-AND-DEPLOYMENT.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md` | Data Isolation and Lifecycle Hunting: Reach for this file when the target stores multi-tenant or access-controlled data, derives search/index/cache/analytics copies, issues object links, exports or restores records, migrates... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/DATA-ISOLATION-AND-LIFECYCLE.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md` | Desktop, Mobile, and Local IPC Hunting: Reach for this file when the target is a desktop or mobile app, privileged helper, updater, local daemon, webview host, deep-link handler, browser native-messaging host, or local IPC... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/DESKTOP-MOBILE-AND-LOCAL-IPC.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/HUNTING.md` | Vulnerability Hunting: The parent assigns planned ledger units to general agents. Use enough focused hunters to cover the units without combining unrelated boundaries. One hunter may own closely related units in one subsystem;... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/HUNTING.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/MEMORY-SAFETY-AND-BINARY.md` | Memory Safety, Binary, and Kernel Hunting: Reach for this file when the target processes untrusted bytes in a memory-unsafe or privileged context: C/C++/Objective-C, Rust unsafe, FFI, kernel modules and drivers, parsers and... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/MEMORY-SAFETY-AND-BINARY.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md` | Protocols, RPC, and Messaging Hunting: Reach for this file when the target uses gRPC, GraphQL transports, Cap'n Proto, Thrift, Protobuf, custom binary protocols, streaming RPC, webhooks, brokers, queues, pub/sub, or event... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/PROTOCOLS-RPC-AND-MESSAGING.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/RECONNAISSANCE.md` | Reconnaissance: The parent initializes run-metadata.json, applies the strict pre-reconnaissance budget gate in SKILL.md, then creates agent scratch roots and the shared ledger before hunting. If the gate fails, record the... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/RECONNAISSANCE.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md` | Resource Exhaustion and Availability Hunting: Reach for this file when untrusted requests, messages, files, tenant state, or agent work can consume CPU, memory, disk, connections, worker slots, paid APIs, or queue capacity, or... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/RESOURCE-EXHAUSTION-AND-AVAILABILITY.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md` | Supply Chain and Release Hunting: Reach for this file when the target resolves dependencies, builds from untrusted contributions, runs CI, creates release artifacts, signs or promotes builds, loads plugins, or updates deployed... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/SUPPLY-CHAIN-AND-RELEASE.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/VALIDATION-AND-REPORTING.md` | Validation, Structured Output, Verification, and Reporting: After the clean coverage-critic pass or an explicitly recorded early stop, consolidate Phase 2 candidates and carried same-source prior confirmations by stable... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/VALIDATION-AND-REPORTING.md before you start." |
| `plugins/code-auditing/security-audit/skills/security-audit/WEB-PROTOCOL-AND-AUTH.md` | HTTP-Protocol and Authentication Hunting: Reach for this file when the target speaks HTTP at a parsing, caching, browser-authentication, or identity boundary: web applications, APIs, reverse proxies, CDNs, gateways, custom... | Guide loaded during the work. Say: "Read plugins/code-auditing/security-audit/skills/security-audit/WEB-PROTOCOL-AND-AUTH.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/security-audit/README.md` | Security Audit: The flagship Aevrin Security skill. It runs a structured, source-first security audit of a codebase and writes validated findings and reports. | Human documentation. Read it for install notes and extra details. |

#### agentic-actions-auditor

Folder: [plugins/code-auditing/agentic-actions-auditor/](plugins/code-auditing/agentic-actions-auditor/)  |  [README](plugins/code-auditing/agentic-actions-auditor/README.md)  |  [AGENTS.md](plugins/code-auditing/agentic-actions-auditor/AGENTS.md)

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations (Claude Code Action, Gemini CLI, OpenAI Codex, GitHub AI Inference)

##### Skill: agentic-actions-auditor

Entry point: `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md`

Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input reaches AI agents running in CI/CD pipelines, including env var intermediary patterns, direct expression injection, dangerous sandbox configurations, and wildcard user allowlists. Use when reviewing workflow files that invoke AI coding agents, auditing CI/CD pipeline security for prompt injection risks, or evaluating agentic action configurations.

Use it when:

- Auditing a repository's GitHub Actions workflows for AI agent security
- Reviewing CI/CD configurations that invoke Claude Code Action, Gemini CLI, or OpenAI Codex
- Checking whether attacker-controlled input can reach AI agent prompts
- Evaluating agentic action configurations (sandbox settings, tool permissions, user allowlists)
- Assessing trigger events that expose workflows to external input (`pull_request_target`, `issue_comment`, etc.)
- Investigating data flow from GitHub event context through `env:` blocks to AI prompt fields

Do not use it when:

- Analyzing workflows that do NOT use any AI agent actions (use general Actions security tools instead)
- Reviewing standalone composite actions or reusable workflows outside of a caller workflow context (use this skill when analyzing a workflow that references them via `uses:`)
- Performing runtime prompt injection testing (this is static analysis guidance, not exploitation)
- Auditing non-GitHub CI/CD systems (Jenkins, GitLab CI, CircleCI)
- Auto-fixing or modifying workflow files (this skill reports findings, does not modify files)

Requests you can copy:

- **Find:** `Use plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md. Scan the GitHub Actions workflows in .github/workflows. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md. Scan the GitHub Actions workflows in .github/workflows. Write a detailed report to ./reports/agentic-actions-auditor.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/agentic-actions-auditor.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md` | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub AI Inference. Detects attack vectors where attacker-controlled input... | Start here. Say: "Follow plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md on the GitHub Actions workflows in .github/workflows." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/action-profiles.md` | Action Security Profiles: Security-relevant configuration fields, default behaviors, dangerous configuration patterns, and remediation guidance for each supported AI action. Referenced by SKILL.md Step 5 for action-specific... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/action-profiles.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/cross-file-resolution.md` | Cross-File Resolution: Composite Actions and Reusable Workflows: AI agents can be hidden inside composite actions and reusable workflows, invisible when analyzing only the caller workflow file. This reference documents how to... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/cross-file-resolution.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/foundations.md` | Shared Foundations: Attacker-Controlled Input Model: This reference documents cross-cutting concepts that all 9 attack vector detection heuristics depend on. Read this before analyzing individual vectors. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/foundations.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-a-env-var-intermediary.md` | Vector A: Env Var Intermediary: Attacker data flows from GitHub event context into env: blocks, and the AI prompt references those env var names -- the AI agent reads the attacker content from environment variables at runtime.... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-a-env-var-intermediary.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-b-direct-expression-injection.md` | Vector B: Direct Expression Injection: Direct ${{ github.event.* }} expressions embedded in AI prompt fields. The YAML engine evaluates the expression at workflow runtime, embedding the attacker's raw text directly into the... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-b-direct-expression-injection.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-c-cli-data-fetch.md` | Vector C: CLI Data Fetch: The prompt instructs the AI agent to fetch attacker-controlled content at runtime using gh CLI commands. The prompt itself may contain no dangerous expressions or env vars with attacker data, but the... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-c-cli-data-fetch.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-d-pr-target-checkout.md` | Vector D: pull_request_target + PR Head Checkout: An attacker opens a fork pull request against a repository that uses pull_request_target to trigger an AI agent workflow. Because pull_request_target runs the workflow... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-d-pr-target-checkout.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-e-error-log-injection.md` | Vector E: Error Log Injection: CI error output, build logs, or test failure messages are fed to an AI agent as context. An attacker crafts code that produces prompt injection payloads in compiler errors, test failure output,... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-e-error-log-injection.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-f-subshell-expansion.md` | Vector F: Subshell Expansion in Restricted Tool Lists: Tool restriction lists include commands that support subshell expansion (e.g., echo), allowing echo $(env) or echo $(whoami) to bypass the restriction and execute... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-f-subshell-expansion.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-g-eval-of-ai-output.md` | Vector G: Eval of AI Output: AI agent response is consumed by a subsequent workflow step that passes it through eval, exec, shell expansion, or other code execution sinks. If an attacker can influence the AI's output (via any... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-g-eval-of-ai-output.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-h-dangerous-sandbox-configs.md` | Vector H: Dangerous Sandbox Configurations: AI action sandbox or safety configurations are set to values that disable protections entirely, giving the AI agent unrestricted shell access, filesystem access, or approval-free... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-h-dangerous-sandbox-configs.md before you start." |
| `plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-i-wildcard-allowlists.md` | Vector I: Wildcard User Allowlists: User allowlist fields are set to wildcard values ("*") that permit ANY GitHub user -- including external contributors, anonymous users, and potential attackers -- to trigger the AI agent.... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/agentic-actions-auditor/skills/agentic-actions-auditor/references/vector-i-wildcard-allowlists.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/agentic-actions-auditor/README.md` | agentic-actions-auditor: Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations. Detects misconfigurations and attack vectors specific to Claude Code Action, Gemini CLI, OpenAI Codex, and GitHub... | Human documentation. Read it for install notes and extra details. |

#### code-understanding

Folder: [plugins/code-auditing/code-understanding/](plugins/code-auditing/code-understanding/)  |  [README](plugins/code-auditing/code-understanding/README.md)  |  [AGENTS.md](plugins/code-auditing/code-understanding/AGENTS.md)

Understand a codebase before looking for bugs in it. Reads it function by function, records what each one assumes and depends on, and saves the write-ups to files instead of filling up the conversation.

##### Skill: code-understanding

Entry point: `plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md`

Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture review on unfamiliar code, and before any vulnerability-hunting pass.

Requests you can copy:

- **Find:** `Use plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md on this repository. List the gaps, risks, and weak spots you find. Do not change any code.`
- **Report:** `Use plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md on this repository. Write a detailed report to ./reports/code-understanding.md with ratings, evidence, and recommended changes.`
- **Fix:** `Read ./reports/code-understanding.md. Apply the recommended changes one at a time, then check each one.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md` | Understand a codebase before looking for bugs in it - what each function assumes, what it guarantees, and what it depends on elsewhere. Use when starting an audit, threat model, or architecture review on unfamiliar code, and... | Start here. Say: "Follow plugins/code-auditing/code-understanding/skills/code-understanding/SKILL.md on this repository." |
| `plugins/code-auditing/code-understanding/skills/code-understanding/resources/ANALYSIS_FORMAT.md` | Analysis Format: The output format for a per-function analysis. The skill body defines what to analyze; this defines how to | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/code-understanding/skills/code-understanding/resources/ANALYSIS_FORMAT.md before you start." |
| `plugins/code-auditing/code-understanding/skills/code-understanding/resources/DOMAIN_NOTES.md` | Domain Notes: The format never changes. Whatever the target, you are always asking the same four questions up front - | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/code-understanding/skills/code-understanding/resources/DOMAIN_NOTES.md before you start." |
| `plugins/code-auditing/code-understanding/skills/code-understanding/resources/FUNCTION_MICRO_ANALYSIS_EXAMPLE.md` | Worked Example: A complete per-function analysis. The subject is C; the format is language-neutral, and the notes at the end | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/code-understanding/skills/code-understanding/resources/FUNCTION_MICRO_ANALYSIS_EXAMPLE.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/code-understanding/agents/function-analyzer.md` | Analyzes one function in depth for audit context: invariants, assumptions, and what its callees establish. Writes the prose analysis to disk and returns a compact record. Use for dense functions, data-flow chains,... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/code-understanding/agents/function-analyzer.md." |
| `plugins/code-auditing/code-understanding/README.md` | Audit Context Building: Understand a codebase before you go looking for bugs in it. | Human documentation. Read it for install notes and extra details. |

#### burpsuite-project-parser

Folder: [plugins/code-auditing/burpsuite-project-parser/](plugins/code-auditing/burpsuite-project-parser/)  |  [README](plugins/code-auditing/burpsuite-project-parser/README.md)  |  [AGENTS.md](plugins/code-auditing/burpsuite-project-parser/AGENTS.md)

Search and extract data from Burp Suite project files (.burp) for security analysis

##### Skill: burpsuite-project-parser

Entry point: `plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md`

Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or analyzing HTTP traffic captured in a Burp project.

Use it when:

- Searching response headers or bodies with regex patterns
- Extracting security audit findings from Burp projects
- Dumping proxy history or site map data
- Analyzing HTTP traffic captured in a Burp project file

Requests you can copy:

- **Use:** `Use plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md on this repository. Write the result and the evidence to ./reports/burpsuite-project-parser.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md` | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex patterns, extracting security audit findings, dumping proxy history or site map data, or... | Start here. Say: "Follow plugins/code-auditing/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/burpsuite-project-parser/commands/burp-search.md` | Searches Burp Suite project files for security analysis | Saved prompt. Say: "Follow plugins/code-auditing/burpsuite-project-parser/commands/burp-search.md on this repository." |
| `plugins/code-auditing/burpsuite-project-parser/README.md` | Burp Suite Project Parser: Search and extract data from Burp Suite project files (.burp) for use in Claude | Human documentation. Read it for install notes and extra details. |

#### c-review

Folder: [plugins/code-auditing/c-review/](plugins/code-auditing/c-review/)  |  [README](plugins/code-auditing/c-review/README.md)  |  [AGENTS.md](plugins/code-auditing/c-review/AGENTS.md)

Comprehensive C/C++ security code review, with coverage verified against a parse of the source

##### Skill: c-review

Entry point: `plugins/code-auditing/c-review/skills/c-review/SKILL.md`

Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for memory safety, or hunting integer overflow / use-after-free / race conditions in userspace code.

Requests you can copy:

- **Find:** `Use plugins/code-auditing/c-review/skills/c-review/SKILL.md. Scan the C/C++ code in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/c-review/skills/c-review/SKILL.md. Scan the C/C++ code in ./src. Write a detailed report to ./reports/c-review.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/c-review.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/c-review/skills/c-review/SKILL.md` | Performs comprehensive C/C++ security review for memory corruption, integer overflows, race conditions, and platform-specific vulnerabilities. Use when auditing native C/C++ applications, reviewing daemons or services for... | Start here. Say: "Follow plugins/code-auditing/c-review/skills/c-review/SKILL.md on the C/C++ code in ./src." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/c-review/agents/c-review-worker.md` | Runs one c-review producing task - a location slice, the class sweep, the invariant audit or the dedup pass - reading source and writing exactly one part file. Spawned by the c-review workflow only; it reads and writes, and... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/c-review/agents/c-review-worker.md." |
| `plugins/code-auditing/c-review/README.md` | c-review: C/C++ security code review. | Human documentation. Read it for install notes and extra details. |

#### differential-review

Folder: [plugins/code-auditing/differential-review/](plugins/code-auditing/differential-review/)  |  [README](plugins/code-auditing/differential-review/README.md)  |  [AGENTS.md](plugins/code-auditing/differential-review/AGENTS.md)

Security-focused differential review of code changes with git history analysis and blast radius estimation

##### Skill: differential-review

Entry point: `plugins/code-auditing/differential-review/skills/differential-review/SKILL.md`

Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting callers, checks test coverage of modified code, and generates a markdown report. Use when reviewing a PR, commit, or diff for security vulnerabilities, checking whether a change re-introduces a previously fixed bug, asking what else a change could break, or finding which modified code has no test covering it.

Do not use it when:

- **Greenfield code** (no baseline to compare)
- **Documentation-only changes** (no security impact)
- **Formatting/linting** (cosmetic changes)
- **User explicitly requests quick summary only** (they accept risk)

Requests you can copy:

- **Find:** `Use plugins/code-auditing/differential-review/skills/differential-review/SKILL.md. Scan the changes between main and my current branch. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/differential-review/skills/differential-review/SKILL.md. Scan the changes between main and my current branch. Write a detailed report to ./reports/differential-review.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/differential-review.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/differential-review/skills/differential-review/SKILL.md` | Performs security-focused differential review of code changes. Adapts analysis depth to codebase size, uses git blame for context, calculates blast radius by counting callers, checks test coverage of modified code, and... | Start here. Say: "Follow plugins/code-auditing/differential-review/skills/differential-review/SKILL.md on the changes between main and my current branch." |
| `plugins/code-auditing/differential-review/skills/differential-review/adversarial.md` | Adversarial Vulnerability Analysis (Phase 5): Structured methodology for finding vulnerabilities through attacker modeling. | Guide loaded during the work. Say: "Read plugins/code-auditing/differential-review/skills/differential-review/adversarial.md before you start." |
| `plugins/code-auditing/differential-review/skills/differential-review/methodology.md` | Differential Review Methodology: Detailed phase-by-phase workflow for security-focused code review. | Guide loaded during the work. Say: "Read plugins/code-auditing/differential-review/skills/differential-review/methodology.md before you start." |
| `plugins/code-auditing/differential-review/skills/differential-review/patterns.md` | Common Vulnerability Patterns: Quick reference for detecting common security issues in code changes. | Guide loaded during the work. Say: "Read plugins/code-auditing/differential-review/skills/differential-review/patterns.md before you start." |
| `plugins/code-auditing/differential-review/skills/differential-review/reporting.md` | Report Generation (Phase 6): Comprehensive markdown report structure and formatting guidelines. | Guide loaded during the work. Say: "Read plugins/code-auditing/differential-review/skills/differential-review/reporting.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/differential-review/agents/adversarial-modeler.md` | Models attacker perspectives and builds exploit scenarios for HIGH RISK code changes. Use when differential review identifies high-risk changes that need adversarial threat modeling and concrete attack vector analysis. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/differential-review/agents/adversarial-modeler.md." |
| `plugins/code-auditing/differential-review/commands/diff-review.md` | Performs security-focused differential review of code changes | Saved prompt. Say: "Follow plugins/code-auditing/differential-review/commands/diff-review.md on the changes between main and my current branch." |
| `plugins/code-auditing/differential-review/README.md` | Differential Review: Security-focused differential review of code changes with git history analysis and blast radius estimation. | Human documentation. Read it for install notes and extra details. |

#### dimensional-analysis

Folder: [plugins/code-auditing/dimensional-analysis/](plugins/code-auditing/dimensional-analysis/)  |  [README](plugins/code-auditing/dimensional-analysis/README.md)  |  [AGENTS.md](plugins/code-auditing/dimensional-analysis/AGENTS.md)

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol. Prevents dimensional mismatches and catches formula bugs early.

##### Skill: dimensional-analysis

Entry point: `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md`

Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol, offchain code, or other blockchain-related codebase with arithmetic. Prevents dimensional mismatches and catches formula bugs early.

Use it when:

- Annotating a codebase with unit/dimension comments (e.g., `D18{tok}`, `D27{UoA/tok}`)
- Performing dimensional analysis on DeFi protocols, financial code, or scientific computations
- Hunting for arithmetic bugs caused by unit mismatches, missing scaling, or precision loss
- Auditing codebases with mixed decimal precisions or fixed-point arithmetic

Do not use it when:

- Codebases with no numeric arithmetic or unit conversions - there is nothing to annotate
- Pure integer counting logic (loop indices, array lengths) with no physical or financial dimensions
- When you only need a quick spot-check of a single formula - read the code directly instead of running the full pipeline

Requests you can copy:

- **Find:** `Use plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md. Scan the contracts or formulas in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md. Scan the contracts or formulas in ./src. Write a detailed report to ./reports/dimensional-analysis.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/dimensional-analysis.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md` | Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a... | Start here. Say: "Follow plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/SKILL.md on the contracts or formulas in ./src." |
| `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/annotate.md` | Step 2: Annotate the Codebase: After defining dimensions (Step 1), add annotations to all numeric values in the code. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/annotate.md before you start." |
| `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/bug-patterns.md` | Dimensional Bug Patterns: This document catalogs common dimensional bugs with examples and detection strategies. Examples use Solidity syntax, but these bug patterns occur in any language performing arithmetic with mixed units... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/bug-patterns.md before you start." |
| `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/common-dimensions.md` | Common Dimensions in DeFi: This document catalogs standard dimensional units used across DeFi protocols. While examples use Solidity syntax, the dimensional vocabulary is protocol-agnostic and applies equally to Rust (Anchor,... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/common-dimensions.md before you start." |
| `plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/dimension-algebra.md` | Dimensional Algebra Rules: This document defines the rules for dimensional arithmetic. While examples use Solidity syntax, these algebraic rules are universal and apply to any language performing fixed-point or scaled arithmetic. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/dimensional-analysis/skills/dimensional-analysis/references/dimension-algebra.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/dimensional-analysis/agents/arithmetic-scanner.md` | Scans repo for files with dimensional arithmetic to scope discovery | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/arithmetic-scanner.md." |
| `plugins/code-auditing/dimensional-analysis/agents/dimension-annotator.md` | Adds dimensional annotations to source code at anchor points using Reserve Protocol's format | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-annotator.md." |
| `plugins/code-auditing/dimensional-analysis/agents/dimension-discoverer.md` | Discovers dimensional vocabulary for codebases by analyzing naming conventions and protocol patterns | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-discoverer.md." |
| `plugins/code-auditing/dimensional-analysis/agents/dimension-propagator.md` | Propagates dimensional annotations through arithmetic and call chains, reporting mismatches found during propagation | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-propagator.md." |
| `plugins/code-auditing/dimensional-analysis/agents/dimension-validator.md` | Validates dimensional consistency and detects dimensional bugs in annotated code | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/dimensional-analysis/agents/dimension-validator.md." |
| `plugins/code-auditing/dimensional-analysis/README.md` | Dimensional Analysis Plugin: Add dimensional annotations to codebases and detect dimensional bugs. Uses an annotation format inspired by Reserve Protocol's Solidity conventions, but applicable to any language or protocol... | Human documentation. Read it for install notes and extra details. |

#### false-positive-check

Folder: [plugins/code-auditing/false-positive-check/](plugins/code-auditing/false-positive-check/)  |  [README](plugins/code-auditing/false-positive-check/README.md)  |  [AGENTS.md](plugins/code-auditing/false-positive-check/AGENTS.md)

Systematic false positive verification for security bug analysis with mandatory gate reviews

##### Skill: false-positive-check

Entry point: `plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md`

Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use when asked whether a specific finding is real, exploitable, or a false positive, or to verify or validate a suspected vulnerability - not for hunting or discovering new bugs.

Use it when:

- "Is this bug real?" or "is this a true positive?"
- "Is this a false positive?" or "verify this finding"
- "Check if this vulnerability is exploitable"
- Any request to verify or validate a specific suspected bug

Do not use it when:

- Finding or hunting for bugs ("find bugs", "security analysis", "audit code")
- General code review for style, performance, or maintainability
- Feature development, refactoring, or non-security tasks
- When the user explicitly asks for a quick scan without verification

Requests you can copy:

- **Check:** `Use plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.`
- **Report:** `Use plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/false-positive-check.md with the verdict and the evidence for it.`
- **Fix:** `Read ./reports/false-positive-check.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md` | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FALSE POSITIVE verdict with documented evidence for each. Use when asked whether a specific finding is real,... | Start here. Say: "Follow plugins/code-auditing/false-positive-check/skills/false-positive-check/SKILL.md on this repository." |
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/references/bug-class-verification.md` | Bug-Class-Specific Verification: Different bug classes require different verification approaches. After classifying the bug in Step 0, apply the class-specific requirements below in addition to the generic verification phases. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/false-positive-check/skills/false-positive-check/references/bug-class-verification.md before you start." |
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/references/deep-verification.md` | Deep Verification: Full task-based verification for complex bugs. Use when routing from SKILL.md selects the deep path, or when standard verification escalates. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/false-positive-check/skills/false-positive-check/references/deep-verification.md before you start." |
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/references/evidence-templates.md` | Evidence Templates: Use these templates when documenting verification evidence for each bug. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/false-positive-check/skills/false-positive-check/references/evidence-templates.md before you start." |
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/references/false-positive-patterns.md` | False Positive Patterns - Lessons Learned: Apply ALL items in this checklist to EACH potential bug during verification. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/false-positive-check/skills/false-positive-check/references/false-positive-patterns.md before you start." |
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/references/gate-reviews.md` | Gate Reviews and Verdicts: Before reporting ANY bug as a vulnerability, all six gate reviews must pass. Evaluate these during the GATE REVIEW task after all phases are complete: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/false-positive-check/skills/false-positive-check/references/gate-reviews.md before you start." |
| `plugins/code-auditing/false-positive-check/skills/false-positive-check/references/standard-verification.md` | Standard Verification: Linear single-pass checklist for straightforward bugs. No task tracking - work through each step sequentially and document findings inline. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/false-positive-check/skills/false-positive-check/references/standard-verification.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/false-positive-check/agents/data-flow-analyzer.md` | Analyzes data flow from source to vulnerability sink, mapping trust boundaries, API contracts, environment protections, and cross-references. Spawned by false-positive-check during Phase 1 verification. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/false-positive-check/agents/data-flow-analyzer.md." |
| `plugins/code-auditing/false-positive-check/agents/exploitability-verifier.md` | Verifies whether a suspected vulnerability is actually exploitable by proving attacker control, mathematical bounds, and race condition feasibility. Spawned by false-positive-check during Phase 2 verification. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/false-positive-check/agents/exploitability-verifier.md." |
| `plugins/code-auditing/false-positive-check/agents/poc-builder.md` | Creates proof-of-concept exploits (pseudocode, executable, and unit tests) demonstrating a verified vulnerability, plus negative PoCs showing exploit preconditions. Spawned by false-positive-check during Phase 4 verification. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/false-positive-check/agents/poc-builder.md." |
| `plugins/code-auditing/false-positive-check/README.md` | false-positive-check: A plugin that enforces systematic false positive verification when verifying suspected security bugs. | Human documentation. Read it for install notes and extra details. |

#### insecure-defaults

Folder: [plugins/code-auditing/insecure-defaults/](plugins/code-auditing/insecure-defaults/)  |  [README](plugins/code-auditing/insecure-defaults/README.md)  |  [AGENTS.md](plugins/code-auditing/insecure-defaults/AGENTS.md)

Detects insecure default configurations including hardcoded credentials, fallback secrets, weak authentication defaults, and dangerous values in production

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/insecure-defaults/commands/audit.md` | Audit a file, directory, or whole repo for insecure default configuration: fallback secrets, default credentials, fail-open switches, weak crypto, permissive access, debug leakage. Parallel sweeps collect candidates, then a... | Saved prompt. Say: "Follow plugins/code-auditing/insecure-defaults/commands/audit.md on this repository." |
| `plugins/code-auditing/insecure-defaults/README.md` | Insecure Defaults Detection: Audits a codebase for insecure default configuration, tracing each candidate before reporting it. | Human documentation. Read it for install notes and extra details. |
| `plugins/code-auditing/insecure-defaults/references/debug-features.md` | Debug and Introspection Defaults: Report when: Internal detail reaches a response, a listening port, or a log a lower-privileged party can read, whether it is gated by a flag that defaults to on, or simply unconditional (a... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/debug-features.md before you start." |
| `plugins/code-auditing/insecure-defaults/references/default-credentials.md` | Default Credentials: Report when: A credential literal that a running deployment can actually authenticate with, including seeded accounts created on first boot. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/default-credentials.md before you start." |
| `plugins/code-auditing/insecure-defaults/references/fail-open-security.md` | Fail-Open Security Switches: Report when: The value taken when configuration is absent disables a security control. The insecure state is the unconfigured state. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/fail-open-security.md before you start." |
| `plugins/code-auditing/insecure-defaults/references/fallback-secrets.md` | Fallback Secrets: Report when: A default value supplied when the env var is absent, where that value feeds signing, encryption, session, or token machinery. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/fallback-secrets.md before you start." |
| `plugins/code-auditing/insecure-defaults/references/permissive-access.md` | Permissive Access Defaults: Report when: Access is granted to a party who should not have it, either because that is the hardcoded value (ACL='public-read', mode 0o666, Access-Control-Allow-Origin '*') or because it is what... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/permissive-access.md before you start." |
| `plugins/code-auditing/insecure-defaults/references/weak-crypto.md` | Weak Cryptographic Defaults: Report when: A broken or non-cryptographic primitive standing in for a security-relevant one: password hashing, token generation, encryption, signature verification. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/insecure-defaults/references/weak-crypto.md before you start." |

#### rust-review

Folder: [plugins/code-auditing/rust-review/](plugins/code-auditing/rust-review/)  |  [README](plugins/code-auditing/rust-review/README.md)  |  [AGENTS.md](plugins/code-auditing/rust-review/AGENTS.md)

Comprehensive Rust security code review with specialized bug-finding agents covering the safe/unsafe boundary, memory safety in unsafe blocks, concurrency, panic-induced DoS, recursion-induced stack overflow, FFI, and async runtime hazards

##### Skill: rust-review

Entry point: `plugins/code-auditing/rust-review/skills/rust-review/SKILL.md`

Performs comprehensive Rust security review for safe/unsafe boundary issues, memory safety in unsafe blocks, concurrency hazards, panic-induced DoS, FFI safety, and async runtime mistakes. Use when auditing Rust crates, services, or libraries - particularly those with `unsafe`, FFI, or concurrent code.

Do not use it when:

- Pure-C / pure-C++ codebases - use `c-review` instead.
- Smart contracts (Solana programs / NEAR contracts / Ink!) - use `solana-vulnerability-scanner` or the contract-specific skill.
- Kernel-mode Rust drivers without userspace allocator - coverage is incomplete; flag as advisory only.
- Secrets/key memory hygiene (zeroization, `Zeroize`/`ZeroizeOnDrop`/`secrecy` usage, lingering stack/heap copies) - use the `secret-wipe-audit` skill; rust-review does not cover memory zeroization.

Requests you can copy:

- **Find:** `Use plugins/code-auditing/rust-review/skills/rust-review/SKILL.md. Scan the Rust crate in this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/rust-review/skills/rust-review/SKILL.md. Scan the Rust crate in this repository. Write a detailed report to ./reports/rust-review.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/rust-review.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/rust-review/skills/rust-review/SKILL.md` | Performs comprehensive Rust security review for safe/unsafe boundary issues, memory safety in unsafe blocks, concurrency hazards, panic-induced DoS, FFI safety, and async runtime mistakes. Use when auditing Rust crates,... | Start here. Say: "Follow plugins/code-auditing/rust-review/skills/rust-review/SKILL.md on the Rust crate in this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/rust-review/agents/rust-review-dedup-judge.md` | Deduplication judge for the rust-review pipeline. Merges duplicate findings deterministically by exact location and bug class, then runs LLM passes over same-function candidates, including the same bug filed under different... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/rust-review/agents/rust-review-dedup-judge.md." |
| `plugins/code-auditing/rust-review/agents/rust-review-fp-judge.md` | Second-stage judge in the rust-review pipeline. Runs after dedup-judge on merged primaries only. Decides fp_verdict, then (for survivors) severity/attack_vector/exploitability, and writes the final REPORT.md + REPORT.sarif.... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/rust-review/agents/rust-review-fp-judge.md." |
| `plugins/code-auditing/rust-review/agents/rust-review-worker.md` | Runs one assigned rust-review cluster task and writes finding files to the run's output directory. Spawned by the rust-review skill orchestrator only. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/rust-review/agents/rust-review-worker.md." |
| `plugins/code-auditing/rust-review/prompts/clusters/async-runtime.md` | Cluster: Async runtime hazards: ID prefixes: ASYNCBLOCK, CANCELSAFETY, SELECTBIAS. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/async-runtime.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/concurrency-data-race.md` | Cluster: Concurrency - data races: A significant share of non-blocking concurrency bugs in Rust occur entirely in safe code via misuse of Atomic* primitives. Unsafe Sync impls add a second front. Cross-process shared memory... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/concurrency-data-race.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/concurrency-locking.md` | Cluster: Concurrency - locking & blocking: Per empirical study, 30/38 Rust deadlocks are double-lock caused by MutexGuard lexical scope misunderstanding. ABBA, condvar, channel starvation, and Once reentrancy round out the... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/concurrency-locking.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/error-handling.md` | Cluster: Error handling flow: ID prefixes: RESDISC, DROPPANIC, LOSSYFROM, LOSSYSTR, BUFFLUSH. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/error-handling.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/ffi-cross-language.md` | Cluster: FFI cross-language: ID prefixes: CSTRDANGLE, ABIMISMATCH, REPRCPAD, OPAQUEPTR, FOREIGNDROP, CLOSUREFFI, DYNFFI. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/ffi-cross-language.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/info-disclosure.md` | Cluster: Information disclosure: Externally observable leaks of internal runtime state the compiler cannot catch: raw memory addresses reaching logs, API responses, serialized output, or error strings, defeating ASLR. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/info-disclosure.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/input-os-safety.md` | Cluster: Input & OS-interaction safety: Safe-code bugs at the boundary with untrusted input and the OS that the compiler cannot catch: path handling, filesystem races. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/input-os-safety.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/layout-safety.md` | Cluster: Type layout safety: Undefined behavior from in-memory type layout the compiler does not always reject: references to fields of #[repr(packed)] structs (including implicit borrows via auto-deref). Common in wire-format... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/layout-safety.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/logic-correctness.md` | Cluster: Logic correctness: ID prefixes: ORDEQHASH, TRAITADV, CLOSUREPANIC, FLOATEDGE, STRCMP, SERFIELDS, NONDET, KEYMUT. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/logic-correctness.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/memory-safety.md` | Cluster: Memory safety (unsafe code): Rust memory-safety bugs ALWAYS originate from unsafe code. Per empirical study, 70 production memory-safety bugs all had a propagation chain across the safe/unsafe boundary. The sub-passes... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/memory-safety.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/panic-dos.md` | Cluster: Panic-induced DoS and availability: Rust panics terminate the thread (or process under panic = "abort"). On servers, an attacker-triggered panic is a DoS. RESEXHAUST runs first: CPU/RAM exhaustion via unbounded loops,... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/panic-dos.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/recursion-dos.md` | Cluster: Recursion-induced stack overflow: Stack overflow is *not* a panic. It cannot be caught with std::panic::catch_unwind, and it aborts the process unconditionally regardless of panic = "abort" / "unwind". On a server, an... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/recursion-dos.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/resource-handling.md` | Cluster: Resource and destructor handling: Non-memory OS resources (file descriptors, handles, sockets) and values whose Drop performs security-relevant cleanup (secrets, connections, transactions) follow the same ownership... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/resource-handling.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/static-hygiene.md` | Cluster: Static hygiene: Project-wide hardening rules. ID prefixes: CARGOLINT, MSRV, DEPRECAPI. | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/static-hygiene.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/clusters/unsafe-boundary.md` | Cluster: Unsafe boundary: Rust's safety guarantees end at unsafe blocks. This cluster maps the attack surface - every public, safe entry point that can transitively reach an unsafe operation - and audits each safe→unsafe... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/clusters/unsafe-boundary.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/abi-mismatch-finder.md` | Detects extern "C" function signatures that disagree with the C header in arg type, count, or return type | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/abi-mismatch-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/adversarial-trait-finder.md` | Detects unsafe code trusting return values from user-supplied trait impls (Read, Iterator, Hash, etc.) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/adversarial-trait-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/arithmetic-overflow-finder.md` | Detects unchecked arithmetic on untrusted integers that panics in debug and silently wraps in release (or panics under overflow-checks=true) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/arithmetic-overflow-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/assertion-reachable-finder.md` | Detects reachable unreachable!()/unimplemented!()/todo!()/assert!() in non-test code | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/assertion-reachable-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/async-blocking-finder.md` | Detects std::sync, std::fs, std::thread::sleep, or other blocking std calls inside async functions | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/async-blocking-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/atomic-race-finder.md` | Detects non-atomic read-modify-write sequences on Atomic* types | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/atomic-race-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/buffer-overflow-unsafe-finder.md` | Detects safe-side index arithmetic flowing into unchecked unsafe memory access | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/buffer-overflow-unsafe-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/bufwriter-unflushed-finder.md` | Detects BufWriter (and other buffered writers) dropped without an explicit flush, silently swallowing write errors | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/bufwriter-unflushed-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/cancel-safety-finder.md` | Detects await points across mutable state mutation that can corrupt on cancellation (select! drop) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/cancel-safety-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/cargo-lint-config-finder.md` | Detects missing or insufficient [lints] configuration in Cargo.toml for security-relevant warnings | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/cargo-lint-config-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/closure-ffi-finder.md` | Detects Rust closures passed to extern "C" callbacks without panic isolation | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/closure-ffi-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/closure-panic-finder.md` | Detects user-supplied closures that can panic across unsafe scaffolding, causing leaks or double-free during unwind | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/closure-panic-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/collection-key-mutation-finder.md` | Detects mutation of live collection keys in HashMap/HashSet/BTreeMap/BinaryHeap that invalidates Hash/Eq/Ord invariants | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/collection-key-mutation-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/cstring-dangling-finder.md` | Detects CString::as_ptr() pointers that escape the CString temporary's statement scope before FFI use | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/cstring-dangling-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/deprecated-api-finder.md` | Detects deprecated unsafe-adjacent APIs (mem::uninitialized, std::intrinsics::*, etc.) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/deprecated-api-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/destructor-skip-finder.md` | Detects process::exit, mem::forget, and ManuallyDrop bypassing Drop for values whose destructor performs security-relevant cleanup | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/destructor-skip-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/double-free-finder.md` | Detects double-free via ptr::read ownership duplication on non-Copy heap types | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/double-free-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/drop-panic-finder.md` | Detects panic possibility inside Drop impls (double-panic abort) or Mutex poisoning paths | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/drop-panic-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/dyn-trait-ffi-finder.md` | Detects fat-pointer trait objects (dyn Trait) crossing extern "C" boundaries | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/dyn-trait-ffi-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/float-edge-finder.md` | Detects NaN/Inf/subnormal handling gaps in float arithmetic on security-relevant paths | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/float-edge-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/foreign-drop-finder.md` | Detects impl Drop on Rust types wrapping FFI-allocated memory that mistakenly calls Rust deallocators | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/foreign-drop-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/invalid-free-finder.md` | Detects invalid-free via assignment to dereferenced pointer over uninitialized memory | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/invalid-free-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/lossy-from-into-finder.md` | Detects From/Into and `as` casts that silently truncate or lose information across security boundaries | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/lossy-from-into-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/lossy-str-conversion-finder.md` | Detects silent lossy UTF-8 / OS-string / path conversions whose U+FFFD substitution corrupts a security-relevant value | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/lossy-str-conversion-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/msrv-mismatch-finder.md` | Detects missing MSRV declaration or use of features past the declared MSRV | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/msrv-mismatch-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/nondeterminism-finder.md` | Detects HashMap/HashSet iteration or other nondeterministic sources feeding determinism-sensitive consumers | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/nondeterminism-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/opaque-pointer-finder.md` | Detects use-after-invalidate or double-free of an opaque FFI handle (handle used or freed again after the C side already freed/destroyed it) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/opaque-pointer-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/ord-eq-hash-finder.md` | Detects manual Ord/PartialOrd/Eq/PartialEq/Hash impls that violate required invariants | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/ord-eq-hash-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/out-of-bounds-index-finder.md` | Detects vec[i] / arr[i] / slice[i] with attacker-controlled index in safe Rust | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/out-of-bounds-index-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/packed-field-ref-finder.md` | Detects undefined behavior from creating references to fields of #[repr(packed)] structs, including implicit borrows via auto-deref | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/packed-field-ref-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/panic-unwind-unsafe-finder.md` | Detects panic-unsafe unsafe container mutation where unwinding leaves stale len/capacity and later Drop/clear causes UAF or double-free | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/panic-unwind-unsafe-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/path-traversal-join-finder.md` | Detects Path::join / PathBuf::push with attacker-controlled components that escape the intended root | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/path-traversal-join-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/pointer-exposure-finder.md` | Detects raw memory addresses leaked to externally observable sinks, defeating ASLR | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/pointer-exposure-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/raw-fd-lifecycle-finder.md` | Detects raw file-descriptor double-close (double drop) and missing-close (leak) ownership errors | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/raw-fd-lifecycle-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/recursive-deserialize-stack-overflow-finder.md` | Detects deserialization of untrusted input into recursive types without an enforced depth limit (bincode/postcard/custom Deserialize, or a codec like serde_json/serde_yaml/toml/ron/ciborium with its default recursion limit... | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/recursive-deserialize-stack-overflow-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/recursive-drop-stack-overflow-finder.md` | Detects recursive types whose implicit Drop walks the structure recursively, causing an uncatchable stack overflow when the type is built from untrusted input | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/recursive-drop-stack-overflow-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/recursive-format-stack-overflow-finder.md` | Detects format/Display/Debug/Serialize/log macros applied to recursive types reachable from untrusted input, where depth-proportional stack growth causes an uncatchable abort | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/recursive-format-stack-overflow-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/refcell-borrow-panic-finder.md` | Detects RefCell borrow/borrow_mut that panics at runtime due to overlapping borrows driven by reentrancy or callbacks | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/refcell-borrow-panic-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/repr-c-padding-finder.md` | Detects #[repr(C)] structs whose padding bytes leak uninitialized memory across FFI | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/repr-c-padding-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/resource-exhaustion-finder.md` | Detects CPU or memory exhaustion DoS on untrusted size/count - unbounded loops, O(n²) amplification, uncapped allocation, unbounded channels | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/resource-exhaustion-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/result-discarded-finder.md` | Detects Result<T,E> silently dropped via `let _ =`, ignoring errors that must propagate | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/result-discarded-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/select-bias-finder.md` | Detects tokio::select!/futures::select! relying on nondeterministic poll order when correctness requires deterministic branch priority | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/select-bias-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/send-sync-bounds-finder.md` | Detects generic APIs missing Send/Sync bounds when crossing threads | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/send-sync-bounds-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/serialize-struct-mismatch-finder.md` | Detects manual Serialize impls where the declared element count diverges from the number of fields actually serialized | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/serialize-struct-mismatch-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/shared-memory-race-finder.md` | Detects unsynchronized cross-process access to shared memory regions (MAP_SHARED mmap, shm_open, memfd) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/shared-memory-race-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/static-mut-race-finder.md` | Detects unsynchronized reads/writes to static mut shared across threads (data race + UB) | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/static-mut-race-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/str-slice-boundary-finder.md` | Detects str range slicing / split_at / truncate at an attacker-controlled byte index that may fall off a UTF-8 char boundary, panicking | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/str-slice-boundary-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/string-comparison-finder.md` | Detects security decisions that use substring/prefix/suffix predicates where full equality is required, or mix case-sensitivity inconsistently | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/string-comparison-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/toctou-finder.md` | Detects filesystem time-of-check/time-of-use races where a path check is separated from the matching open/create/remove | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/toctou-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/uninitialized-read-finder.md` | Detects reads from uninitialized memory in Rust unsafe blocks | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/uninitialized-read-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/union-ub-finder.md` | Detects undefined behavior from union variant misreads and lifetime extension through union fields | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/union-ub-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/unsafe-sync-impl-finder.md` | Audits unsafe impl Send/Sync over types with interior mutability | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/unsafe-sync-impl-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/unwrap-on-untrusted-finder.md` | Detects unwrap/expect on Result/Option flowing from attacker-controlled input | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/unwrap-on-untrusted-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/use-after-free-finder.md` | Detects use-after-free via raw pointers escaping implicit Drop scope in Rust | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/use-after-free-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/prompts/general/vec-set-len-uninit-finder.md` | Detects Vec length advanced without initializing new elements, exposing uninitialized memory through safe Rust APIs | Prompt part used by the review workflow. Say: "Use plugins/code-auditing/rust-review/prompts/general/vec-set-len-uninit-finder.md as the prompt for that pass." |
| `plugins/code-auditing/rust-review/README.md` | rust-review: Rust security code review plugin. Bug-class coverage comes from empirical bug-shape research across 245 memory-corruption, 177 unsound safe-API, 150 denial-of-service, and 60 thread-safety advisories in the... | Human documentation. Read it for install notes and extra details. |

#### semgrep-rule-creator

Folder: [plugins/code-auditing/semgrep-rule-creator/](plugins/code-auditing/semgrep-rule-creator/)  |  [README](plugins/code-auditing/semgrep-rule-creator/README.md)  |  [AGENTS.md](plugins/code-auditing/semgrep-rule-creator/AGENTS.md)

Create custom Semgrep rules for detecting bug patterns and security vulnerabilities

##### Skill: semgrep-rule-creator

Entry point: `plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md`

Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections.

Use it when:

- Writing Semgrep rules for specific bug patterns
- Writing rules to detect security vulnerabilities in your codebase
- Writing taint mode rules for data flow vulnerabilities
- Writing rules to enforce coding standards

Do not use it when:

- Running existing Semgrep rulesets
- General static analysis without custom rules (use `static-analysis` skill)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md on this repository. Write the result and the evidence to ./reports/semgrep-rule-creator.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md` | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or building custom static analysis detections. | Start here. Say: "Follow plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md on this repository." |
| `plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/references/quick-reference.md` | Semgrep Rule Quick Reference: Constrain metavariables to specific types (reduces false positives): | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/references/quick-reference.md before you start." |
| `plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/references/workflow.md` | Semgrep Rule Creation Workflow: Detailed workflow for creating production-quality Semgrep rules. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/semgrep-rule-creator/skills/semgrep-rule-creator/references/workflow.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/semgrep-rule-creator/commands/semgrep-rule.md` | Creates Semgrep rules with test-first methodology | Saved prompt. Say: "Follow plugins/code-auditing/semgrep-rule-creator/commands/semgrep-rule.md on this repository." |
| `plugins/code-auditing/semgrep-rule-creator/README.md` | Semgrep Rule Creator: Create production-quality Semgrep rules for detecting bug patterns and security vulnerabilities. | Human documentation. Read it for install notes and extra details. |

#### semgrep-rule-variant-creator

Folder: [plugins/code-auditing/semgrep-rule-variant-creator/](plugins/code-auditing/semgrep-rule-variant-creator/)  |  [README](plugins/code-auditing/semgrep-rule-variant-creator/README.md)  |  [AGENTS.md](plugins/code-auditing/semgrep-rule-variant-creator/AGENTS.md)

Creates language variants of existing Semgrep rules with proper applicability analysis and test-driven validation

##### Skill: semgrep-rule-variant-creator

Entry point: `plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md`

Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each language.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md on this repository. Write the result and the evidence to ./reports/semgrep-rule-variant-creator.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md` | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rule and target languages as input, produces independent rule+test directories for each... | Start here. Say: "Follow plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md on this repository." |
| `plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/references/applicability-analysis.md` | Applicability Analysis: Phase 1 of the variant creation workflow. Before porting a rule, analyze whether the vulnerability pattern applies to the target language. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/references/applicability-analysis.md before you start." |
| `plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/references/language-syntax-guide.md` | Language Syntax Translation Guide: Guidance for translating Semgrep patterns between languages. This is NOT a pre-built mapping-use these principles to research and adapt patterns for your specific case. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/references/language-syntax-guide.md before you start." |
| `plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/references/workflow.md` | Variant Creation Mechanics and Troubleshooting: The orchestration lives in workflows/port-rule-to-languages.js at the plugin root, which | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/references/workflow.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/semgrep-rule-variant-creator/README.md` | Semgrep Rule Variant Creator: A Claude Code skill for porting existing Semgrep rules to new target languages with proper applicability analysis and test-driven validation. | Human documentation. Read it for install notes and extra details. |

#### risky-apis

Folder: [plugins/code-auditing/risky-apis/](plugins/code-auditing/risky-apis/)  |  [README](plugins/code-auditing/risky-apis/README.md)  |  [AGENTS.md](plugins/code-auditing/risky-apis/AGENTS.md)

Identify error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes

##### Skill: risky-apis

Entry point: `plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md`

Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code follows 'secure by default' and 'pit of success' principles. Triggers: footgun, misuse-resistant, secure defaults, API usability, dangerous configuration.

Use it when:

- Reviewing API or library design decisions
- Auditing configuration schemas for dangerous options
- Evaluating cryptographic API ergonomics
- Assessing authentication/authorization interfaces
- Reviewing any code that exposes security-relevant choices to developers

Do not use it when:

- Implementation bugs (use standard code review)
- Business logic flaws (use domain-specific analysis)
- Performance optimization (different concern)

Requests you can copy:

- **Find:** `Use plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md. Scan the APIs and configuration in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md. Scan the APIs and configuration in ./src. Write a detailed report to ./reports/risky-apis.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/risky-apis.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md` | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes. Use when reviewing API designs, configuration schemas, cryptographic library ergonomics, or evaluating whether code... | Start here. Say: "Follow plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md on the APIs and configuration in ./src." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/auth-patterns.md` | Authentication & Session Footguns: Patterns that make authentication and session management error-prone. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/auth-patterns.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/case-studies.md` | Real-World Case Studies: Analysis of sharp edges in widely-used libraries. These aren't implementation bugs-they're design decisions that make secure usage difficult. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/case-studies.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/config-patterns.md` | Configuration Security Patterns: Dangerous configuration patterns that enable security failures. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/config-patterns.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/crypto-apis.md` | Cryptographic API Footguns: Detailed patterns for identifying misuse-prone cryptographic interfaces. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/crypto-apis.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-c.md` | C/C++ Sharp Edges: The Problem: Signed integer overflow is undefined behavior. Compilers assume it never happens and optimize accordingly-including removing overflow checks. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-c.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-csharp.md` | C# Sharp Edges: Fix: Enable NRT AND treat warnings as errors: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-csharp.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-go.md` | Go Sharp Edges: The Problem: Unlike Rust (debug panics), Go silently wraps. Fuzzing with go-fuzz may never find overflow bugs because they don't crash. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-go.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-java.md` | Java Sharp Edges: Fix: Always use .equals() for object comparison: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-java.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-javascript.md` | JavaScript / TypeScript Sharp Edges: Fix: Always use === for strict equality. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-javascript.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-kotlin.md` | Kotlin Sharp Edges: Fix: Explicitly declare nullability when calling Java: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-kotlin.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-php.md` | PHP Sharp Edges: Fix: Use strict comparison ===: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-php.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-python.md` | Python Sharp Edges: The Problem: Default arguments are evaluated once at function definition, not at each call. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-python.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-ruby.md` | Ruby Sharp Edges: Real Vulnerabilities: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-ruby.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-rust.md` | Rust Sharp Edges: The Problem: Behavior differs between debug and release. Bugs may only manifest in production. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-rust.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-swift.md` | Swift Sharp Edges: Fix: Use optional binding or nil-coalescing: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/lang-swift.md before you start." |
| `plugins/code-auditing/risky-apis/skills/risky-apis/references/language-specific.md` | Language-Specific Sharp Edges: General programming footguns by language-not limited to cryptography. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/risky-apis/skills/risky-apis/references/language-specific.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/risky-apis/agents/risky-apis-analyzer.md` | Evaluates APIs, configurations, and library interfaces for misuse resistance and footgun potential. Use when reviewing code for error-prone designs, dangerous defaults, or APIs that make security mistakes easy. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/risky-apis/agents/risky-apis-analyzer.md." |
| `plugins/code-auditing/risky-apis/README.md` | Sharp Edges: Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes through developer confusion, laziness, or malice. | Human documentation. Read it for install notes and extra details. |

#### static-analysis

Folder: [plugins/code-auditing/static-analysis/](plugins/code-auditing/static-analysis/)  |  [README](plugins/code-auditing/static-analysis/README.md)  |  [AGENTS.md](plugins/code-auditing/static-analysis/AGENTS.md)

Static analysis toolkit with CodeQL, Semgrep, and SARIF parsing for security vulnerability detection

##### Skill: codeql

Entry point: `plugins/code-auditing/static-analysis/skills/codeql/SKILL.md`

Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build codeql database", "SAST scan", "taint analysis", "dataflow analysis", or "find vulnerabilities in this repo". Covers Python, JavaScript/TypeScript, Go, Java/Kotlin, C/C++, C#, Ruby, and Swift. Supports "run all" (security-and-quality + security-experimental) and "important only" (high-precision) scan modes, and creates data extension models for project-specific sources and sinks. For fast single-file pattern matching, or when no build is available for a compiled language, use the semgrep skill; to parse SARIF that already exists rather than produce it, use the sarif-parsing skill.

Requests you can copy:

- **Find:** `Use plugins/code-auditing/static-analysis/skills/codeql/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/static-analysis/skills/codeql/SKILL.md. Scan this repository. Write a detailed report to ./reports/codeql.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/codeql.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/static-analysis/skills/codeql/SKILL.md` | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on "run codeql", "codeql scan", "build codeql database", "SAST scan", "taint analysis", "dataflow... | Start here. Say: "Follow plugins/code-auditing/static-analysis/skills/codeql/SKILL.md on this repository." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/build-fixes.md` | Build Fixes: Fixes to apply when a CodeQL database build method fails. Try these in order, then retry the current build method. Log each fix attempt. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/build-fixes.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/diagnostic-query-templates.md` | Diagnostic Query Templates: Language-specific QL queries for enumerating sources and sinks recognized by CodeQL. Used during the data extensions creation process. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/diagnostic-query-templates.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/extension-yaml-format.md` | Data Extension YAML Format: YAML format for CodeQL data extension files. Used by the create-data-extensions workflow to model project-specific sources, sinks, and flow summaries. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/extension-yaml-format.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/important-only-suite.md` | Important-Only Query Suite: In important-only mode, generate a custom .qls query suite file at runtime. This applies the same precision/severity filtering to all packs (official + third-party). | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/important-only-suite.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/language-details.md` | Language-Specific Guidance: Commands below assume $DB_NAME and $CODEQL_LANG from the build-database workflow. They | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/language-details.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/macos-arm64e-workaround.md` | macOS arm64e Workaround: Methods for building CodeQL databases on macOS Apple Silicon when the arm64e/arm64 architecture mismatch causes SIGKILL (exit code 137) during build tracing. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/macos-arm64e-workaround.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/performance-tuning.md` | Performance Tuning: All three are set on codeql database analyze "$DB_NAME". CODEQL_RAM is an environment | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/performance-tuning.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/quality-assessment.md` | Quality Assessment: How to assess and improve CodeQL database quality after a successful build. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/quality-assessment.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/ruleset-catalog.md` | Ruleset Catalog: Usage: codeql/<lang>-queries:codeql-suites/<lang>-security-extended.qls | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/ruleset-catalog.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/run-all-suite.md` | Run-All Query Suite: In run-all mode, generate a custom .qls query suite file at runtime. It runs the security-and-quality and security-experimental suites of every installed pack, which is a much wider selection than the... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/run-all-suite.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/sarif-processing.md` | SARIF Processing: jq commands for processing CodeQL SARIF output. Used in the run-analysis workflow Step 5. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/sarif-processing.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/references/threat-models.md` | Threat Models Reference: Control which source categories are active during CodeQL analysis. By default, only remote sources are tracked. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/codeql/references/threat-models.md before you start." |
| `plugins/code-auditing/static-analysis/skills/codeql/workflows/build-database.md` | Build Database Workflow: Create high-quality CodeQL databases by trying build methods in sequence until one produces good results. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/code-auditing/static-analysis/skills/codeql/workflows/build-database.md and run that phase." |
| `plugins/code-auditing/static-analysis/skills/codeql/workflows/create-data-extensions.md` | Create Data Extensions Workflow: Generate data extension YAML files to improve CodeQL's data flow coverage for project-specific APIs. Runs after database build and before analysis. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/code-auditing/static-analysis/skills/codeql/workflows/create-data-extensions.md and run that phase." |
| `plugins/code-auditing/static-analysis/skills/codeql/workflows/run-analysis.md` | Run Analysis Workflow: Execute CodeQL security queries on an existing database with ruleset selection and result formatting. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/code-auditing/static-analysis/skills/codeql/workflows/run-analysis.md and run that phase." |

##### Skill: sarif-parsing

Entry point: `plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md`

Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans - use the Semgrep or CodeQL skills for that.

Use it when:

- Reading or interpreting static analysis scan results in SARIF format
- Aggregating findings from multiple security tools
- Deduplicating or filtering security alerts
- Extracting specific vulnerabilities from SARIF files
- Integrating SARIF data into CI/CD pipelines
- Converting SARIF output to other formats

Do not use it when:

- Running static analysis scans (use CodeQL or Semgrep skills instead)
- Writing CodeQL or Semgrep rules (use their respective skills)
- Analyzing source code directly (SARIF is for processing existing scan results)
- Triaging findings without SARIF input (use similar-bug-finder or audit skills)

Requests you can copy:

- **Find:** `Use plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md. Scan this repository. Write a detailed report to ./reports/sarif-parsing.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/sarif-parsing.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md` | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on "parse sarif", "read scan results", "aggregate findings", "deduplicate alerts", or "process sarif output".... | Start here. Say: "Follow plugins/code-auditing/static-analysis/skills/sarif-parsing/SKILL.md on this repository." |
| `plugins/code-auditing/static-analysis/skills/sarif-parsing/resources/jq-queries.md` | SARIF jq Query Reference: Ready-to-use jq queries for common SARIF parsing tasks. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/sarif-parsing/resources/jq-queries.md before you start." |

##### Skill: semgrep

Entry point: `plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md`

Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and merges the output to SARIF. Supports two scan modes, "run all" for full ruleset coverage and "important only" for security findings at medium-to-high confidence and impact. Uses Semgrep Pro for cross-file taint analysis when it is available. Use when asked to scan code for vulnerabilities, run a security audit with Semgrep, find bugs, or perform static analysis. For the same scan without the approval gate, use the /static-analysis:semgrep-scan workflow.

Use it when:

- Security audit of a codebase
- Finding vulnerabilities before code review
- Scanning for known bug patterns
- First-pass static analysis

Do not use it when:

- Binary analysis → Use binary analysis tools
- Already have Semgrep CI configured → Use existing pipeline
- Need cross-file analysis but no Pro license → Consider CodeQL as alternative
- Creating custom Semgrep rules → Use `semgrep-rule-creator` skill
- Porting existing rules to other languages → Use `semgrep-rule-variant-creator` skill

Requests you can copy:

- **Find:** `Use plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md. Scan this repository. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md. Scan this repository. Write a detailed report to ./reports/semgrep.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/semgrep.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md` | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and... | Start here. Say: "Follow plugins/code-auditing/static-analysis/skills/semgrep/SKILL.md on this repository." |
| `plugins/code-auditing/static-analysis/skills/semgrep/references/rulesets.md` | Semgrep Rulesets Reference: Follow this algorithm to select rulesets based on detected languages and frameworks. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/semgrep/references/rulesets.md before you start." |
| `plugins/code-auditing/static-analysis/skills/semgrep/references/scan-modes.md` | Scan Modes Reference: Full scan with all rulesets and severity levels. Current default behavior. No filtering applied - all findings are reported and triaged. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/static-analysis/skills/semgrep/references/scan-modes.md before you start." |
| `plugins/code-auditing/static-analysis/skills/semgrep/workflows/scan-workflow.md` | Semgrep Scan Workflow: Complete 5-step scan execution process. Read from start to finish and follow each step in order. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/code-auditing/static-analysis/skills/semgrep/workflows/scan-workflow.md and run that phase." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/static-analysis/README.md` | Static Analysis: A comprehensive static analysis toolkit with CodeQL, Semgrep, and SARIF parsing for security vulnerability detection. | Human documentation. Read it for install notes and extra details. |

#### supply-chain-risk-auditor

Folder: [plugins/code-auditing/supply-chain-risk-auditor/](plugins/code-auditing/supply-chain-risk-auditor/)  |  [README](plugins/code-auditing/supply-chain-risk-auditor/README.md)  |  [AGENTS.md](plugins/code-auditing/supply-chain-risk-auditor/AGENTS.md)

Audit a project's npm, PyPI, and Go dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned upstreams, npm publisher concentration, and install scripts

##### Skill: supply-chain-risk-auditor

Entry point: `plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md`

Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script execution. Use when asked to audit dependencies, assess supply-chain or third-party package risk, or review a dependency tree before an engagement.

Do not use it when:

- License compliance auditing.
- Scanning the target's own source for vulnerabilities or secrets - this skill never
- Judging whether the project installs or builds. The audit is designed to work from
- Ecosystems other than npm, PyPI, and Go; say the ecosystem is unsupported rather than

Requests you can copy:

- **Find:** `Use plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md. Scan the dependencies of this project. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md. Scan the dependencies of this project. Write a detailed report to ./reports/supply-chain-risk-auditor.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/supply-chain-risk-auditor.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md` | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned or archived upstreams, npm publisher concentration, and install-time script... | Start here. Say: "Follow plugins/code-auditing/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md on the dependencies of this project." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/supply-chain-risk-auditor/README.md` | Supply Chain Risk Auditor: Generate a supply-chain risk report for a project's direct dependencies across npm, | Human documentation. Read it for install notes and extra details. |

#### similar-bug-finder

Folder: [plugins/code-auditing/similar-bug-finder/](plugins/code-auditing/similar-bug-finder/)  |  [README](plugins/code-auditing/similar-bug-finder/README.md)  |  [AGENTS.md](plugins/code-auditing/similar-bug-finder/AGENTS.md)

Find similar vulnerabilities and bugs across codebases using pattern-based analysis

##### Skill: similar-bug-finder

Entry point: `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md`

Hunts for the other instances of a bug already found - the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or bad pattern turns up in a specific file and the question becomes where else it occurs, including the bare conversational form ("are there others like this?", "is this the same bug?"). Also for generalizing one known instance into a CodeQL or Semgrep query for its whole pattern family, and for triaging a set of look-alike candidates against a known root cause. Not for initial discovery with no bug in hand.

Use it when:

- A vulnerability has been found and you need to search for similar instances
- Building or refining CodeQL/Semgrep queries for security patterns
- Performing systematic code audits after an initial issue discovery
- Analyzing how a single root cause manifests in different code paths

Do not use it when:

- Initial vulnerability discovery - use code-understanding or a domain-specific audit
- General code review with no known pattern to search for
- Writing fix recommendations - use issue-writer
- Understanding unfamiliar code - use code-understanding first

Requests you can copy:

- **Find:** `Use plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md. Scan this repository, starting from the bug I describe. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md. Scan this repository, starting from the bug I describe. Write a detailed report to ./reports/similar-bug-finder.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/similar-bug-finder.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md` | Hunts for the other instances of a bug already found - the variants of one root cause across a codebase. Use immediately after a vulnerability, logic bug, or bad pattern turns up in a specific file and the question becomes... | Start here. Say: "Follow plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/SKILL.md on this repository, starting from the bug I describe." |
| `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/reporting.md` | Reporting a Variant Hunt: Advice for the final stage. The report is written for a security engineer that is reviewing vulnerability variants. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/reporting.md before you start." |
| `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/root-cause.md` | Root Cause and Expansion Axes: Strategy for the first stage of a variant hunt: turning one known bug into the set of | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/root-cause.md before you start." |
| `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/searching.md` | Searching: The Abstraction Ladder: Strategy for the sweep stage. You have a root cause and one axis to search. The job is to | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/searching.md before you start." |
| `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/triage.md` | Triage: Deciding Whether a Candidate Is Real: Strategy for the verification stage. You have candidate locations that resemble a known | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/references/triage.md before you start." |
| `plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/resources/variant-report-template.md` | Variant Analysis Report: Root Cause: [e.g., "User input reaches SQL query without parameterization"] | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/similar-bug-finder/skills/similar-bug-finder/resources/variant-report-template.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/similar-bug-finder/README.md` | Variant Analysis: Find similar vulnerabilities and bugs across codebases using pattern-based analysis. | Human documentation. Read it for install notes and extra details. |

#### report-triage

Folder: [plugins/code-auditing/report-triage/](plugins/code-auditing/report-triage/)  |  [README](plugins/code-auditing/report-triage/README.md)  |  [AGENTS.md](plugins/code-auditing/report-triage/AGENTS.md)

Principled framework for triaging vulnerability reports using 7 brocards (rules of thumb). Evaluates incoming CVEs, bug bounty submissions, and security findings against structured dismissal/acceptance criteria before escalating to deeper analysis.

##### Skill: report-triage

Entry point: `plugins/code-auditing/report-triage/skills/report-triage/SKILL.md`

This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid", "review a security finding", "dismiss a vulnerability", "should we fix this CVE", "prioritize a vulnerability report", or needs to determine whether an incoming vulnerability report warrants investigation. Applies 7 brocards (rules of thumb) to systematically accept, dismiss, or request more information on vulnerability reports, or needs to filter raw findings from agentic vulnerability discovery pipelines before human review.

Use it when:

- Filtering findings from agentic vulnerability discovery pipelines
- Triaging findings during a ToB audit to decide which warrant
- Evaluating third-party CVEs or advisories against a codebase under
- Reviewing bug bounty submissions or external vulnerability reports
- Providing structured, defensible justification when recommending a

Do not use it when:

- **Hunting for new bugs during an audit** -- use other skills
- **Proving exploitability of a confirmed finding** -- use a
- **Triaging fuzzer crashes in C/C++** -- use a dedicated crash

Requests you can copy:

- **Check:** `Use plugins/code-auditing/report-triage/skills/report-triage/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.`
- **Report:** `Use plugins/code-auditing/report-triage/skills/report-triage/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/report-triage.md with the verdict and the evidence for it.`
- **Fix:** `Read ./reports/report-triage.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/report-triage/skills/report-triage/SKILL.md` | This skill should be used when the user asks to "triage a vulnerability report", "assess a CVE", "evaluate a bug bounty submission", "decide if a finding is valid", "review a security finding", "dismiss a vulnerability",... | Start here. Say: "Follow plugins/code-auditing/report-triage/skills/report-triage/SKILL.md on this repository." |
| `plugins/code-auditing/report-triage/skills/report-triage/references/brocards-detail.md` | Brocards for Vulnerability Triage -- Detailed Reference: Expanded explanations, concrete examples, and edge cases for each of the | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/report-triage/skills/report-triage/references/brocards-detail.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/report-triage/README.md` | report-triage: Principled framework for triaging vulnerability reports using 7 brocards | Human documentation. Read it for install notes and extra details. |

#### codegraph

Folder: [plugins/code-auditing/codegraph/](plugins/code-auditing/codegraph/)  |  [README](plugins/code-auditing/codegraph/README.md)  |  [AGENTS.md](plugins/code-auditing/codegraph/AGENTS.md)

Builds source and binary code graphs for security analysis, context slicing, mutation testing, cryptographic protocol modeling, finding triage, and variant analysis.

##### Skill: audit-augmentation

Entry point: `plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md`

Augments Codegraph code graphs with external audit findings from SARIF static analysis results, AuditNotes annotation files, and version-gated Codegraph 0.4.x binary-analysis graph exports. Maps findings to graph nodes by file and line overlap, creates severity-based subgraphs, and enables cross-referencing findings with pre-analysis data (blast radius, taint, etc.). Use when projecting SARIF results onto a code graph, overlaying AuditNotes annotations, importing binary graph findings, cross-referencing Semgrep, CodeQL, or binary-analysis findings with call graph data, or visualizing audit findings in the context of code structure.

Use it when:

- Importing Semgrep, CodeQL, or other SARIF-producing tool results into a graph
- Importing AuditNotes audit annotations into a graph
- Importing binary-analysis graph data into a source graph (Codegraph 0.4.0+)
- Cross-referencing static analysis findings with blast radius or taint data
- Querying which functions have high-severity findings
- Visualizing audit coverage alongside code structure
- Preparing one SARIF or AuditNotes result for `codegraph-finding-triage`

Do not use it when:

- Running static analysis tools (use semgrep/codeql directly, then import)
- Building the code graph itself (use the `codegraph` skill)
- Generating diagrams (use the `diagramming-code` skill after augmenting)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md on this repository. Write the result and the evidence to ./reports/audit-augmentation.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md` | Augments Codegraph code graphs with external audit findings from SARIF static analysis results, AuditNotes annotation files, and version-gated Codegraph 0.4.x binary-analysis graph exports. Maps findings to graph nodes by file... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/audit-augmentation/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/audit-augmentation/references/formats.md` | SARIF and AuditNotes Format Reference: SARIF (Static Analysis Results Interchange Format) is an OASIS standard for | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/audit-augmentation/references/formats.md before you start." |

##### Skill: codegraph

Entry point: `plugins/code-auditing/codegraph/skills/codegraph/SKILL.md`

Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, entry point enumeration, proxy/unresolved-call tracking, type/reference queries, structural traversal, graph diffs, audit augmentation, declared cross-language/FFI/external links via `.codegraph/links.toml`, and SQL schema graphs. Use when analyzing call paths, mapping attack surface, finding complexity hotspots, enumerating entry points, tracing taint propagation, measuring blast radius, importing SARIF/AuditNotes/binary findings, linking source graphs across language or RPC boundaries, or building a code graph for audit prioritization. Feature-gate version-specific Codegraph APIs before using them; prefer `codegraph.parse.detect_languages()` or `--language auto` when the target language is unknown or polyglot.

Use it when:

- Mapping call paths from user input to sensitive functions
- Finding complexity hotspots for audit prioritization
- Identifying attack surface and entrypoints
- Understanding call relationships in unfamiliar codebases
- Security review or audit preparation across polyglot projects
- Adding LLM-inferred annotations (assumptions, preconditions) to code units
- Importing external binary-analysis graphs to connect source and binary views

Do not use it when:

- Single-file scripts where call graph adds no value (read the file directly)
- Architecture diagrams not derived from code (use the `diagramming-code` skill or draw by hand)
- Mutation testing triage (use the mutation-triage skill, which calls codegraph internally)
- Runtime behavior analysis (codegraph is static, not dynamic)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/codegraph/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/codegraph/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/codegraph/SKILL.md` | Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, entry point enumeration, proxy/unresolved-call... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/codegraph/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/codegraph/references/preanalysis-passes.md` | Pre-Analysis Passes: Four passes that enrich the code graph before downstream skills (mutation-triage, | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph/references/preanalysis-passes.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph/references/query-patterns.md` | Codegraph Query Patterns for Security Analysis: Common patterns for using Codegraph in security reviews. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph/references/query-patterns.md before you start." |

##### Skill: codegraph-finding-triage

Entry point: `plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md`

Performs graph-assisted triage of a single security finding, SARIF result, AuditNotes annotation, suspicious function, or report excerpt using Codegraph reachability, entrypoint paths, taint, privilege-boundary, blast-radius, caller/callee, and neighborhood evidence. Use when deciding whether one candidate issue is reachable, prioritizing a finding before PoC work, preparing evidence for exploit validation, or checking whether a static-analysis result is actionable.

Use it when:

- Triage one static-analysis result before spending PoC time
- Check whether a manual finding is entrypoint-reachable
- Build an evidence packet for PoC work
- Review a single suspicious function discovered during manual audit
- Decide whether one issue should be promoted, deprioritized, or treated as

Do not use it when:

- Multiple weak findings might compose into a stronger chain. Use a chain or
- The user wants a full audit. Use an audit or design-review workflow instead.
- The user wants remediation verification for a known finding. Use a
- The target is a PR or branch diff. Use `graph-evolution` plus a differential
- No concrete finding, function, file/line, or suspicious sink exists yet. Use

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-finding-triage.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md` | Performs graph-assisted triage of a single security finding, SARIF result, AuditNotes annotation, suspicious function, or report excerpt using Codegraph reachability, entrypoint paths, taint, privilege-boundary, blast-radius,... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/codegraph-finding-triage/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/codegraph-finding-triage/references/input-normalization.md` | Input Normalization: Normalize every request into one candidate record before graph analysis. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-finding-triage/references/input-normalization.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph-finding-triage/references/output-format.md` | Output Format: Return a concise evidence packet. Use Markdown unless the user asks for JSON. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-finding-triage/references/output-format.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph-finding-triage/references/query-recipes.md` | Query Recipes: Use these recipes after building a graph and running engine.preanalysis(). | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-finding-triage/references/query-recipes.md before you start." |

##### Skill: codegraph-review-gate

Entry point: `plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md`

Runs a Codegraph structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed validation or authorization calls, privilege-boundary drift, blast-radius growth, complexity growth, and newly reachable sensitive sinks. Use when reviewing a PR, branch, remediation commit, or release diff where graph-level security regressions should be checked before merge.

Use it when:

- Reviewing a branch, pull request, release diff, or fix commit
- Checking whether a change expands attack surface
- Looking for removed validation or authorization on reachable paths
- Comparing before/after taint, privilege-boundary, blast-radius, or
- Producing graph evidence for a differential review

Do not use it when:

- Single-snapshot analysis. Use `codegraph` or `codegraph-structural`.
- Text-diff review only. Use `differential-review`.
- Full vulnerability discovery. Use an audit or bug-finding workflow.
- One static finding. Use `codegraph-finding-triage`.
- Tooling is unavailable and the user wants manual review only.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-review-gate.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md` | Runs a Codegraph structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed validation or authorization calls, privilege-boundary drift,... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/codegraph-review-gate/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/codegraph-review-gate/references/gate-rules.md` | Gate Rules: Start with deterministic, conservative rules. A triggered rule creates a | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-review-gate/references/gate-rules.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph-review-gate/references/output-format.md` | Output Format: Use Markdown unless the user asks for JSON. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-review-gate/references/output-format.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph-review-gate/references/review-integration.md` | Review Integration: Use the review gate packet as supporting evidence for a human branch review. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-review-gate/references/review-integration.md before you start." |

##### Skill: codegraph-structural

Entry point: `plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md`

Runs full Codegraph structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface, and version-gated Codegraph 0.4+/0.5+ data such as proxy counts, subgraph edges, type/reference summaries, and entrypoint attributes. Use when vivisect needs detailed structural data for a target. Triggers: structural analysis, blast radius, taint analysis, complexity hotspots, proxy nodes, type references.

Use it when:

- Vivisect Phase 1 needs full structural data (hotspots, taint, blast radius, privilege boundaries)
- Detailed pre-analysis passes for a specific target scope
- Generating complexity and taint data for audit prioritization
- Inspecting proxy/unresolved-call counts, subgraph edges, or type-reference

Do not use it when:

- Quick overview only (use `codegraph-summary` instead)
- Ad-hoc code graph queries (use the main `codegraph` skill directly)
- Target is a single small file where structural analysis adds no value

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-structural.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md` | Runs full Codegraph structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface, and version-gated Codegraph 0.4+/0.5+ data such as proxy... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/codegraph-structural/SKILL.md on this repository." |

##### Skill: codegraph-summary

Entry point: `plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md`

Runs a Codegraph summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: codegraph summary, code summary, structural overview.

Use it when:

- Vivisect Phase 0 needs a quick structural overview before decomposition
- Galvanize Phase 1 needs detected languages and entry point count
- Quick orientation on an unfamiliar codebase before deeper analysis

Do not use it when:

- Full structural analysis with all passes needed (use `codegraph-structural`)
- Detailed code graph queries (use the main `codegraph` skill directly)
- You need hotspot scores or taint data (use `codegraph-structural`)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-summary.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md` | Runs a Codegraph summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview. Triggers: codegraph summary, code... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/codegraph-summary/SKILL.md on this repository." |

##### Skill: codegraph-variant-neighborhood

Entry point: `plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md`

Expands one confirmed or suspected vulnerability into a Codegraph graph neighborhood of variant candidates by finding sibling functions, shared callers and callees, common sensitive sinks, common entrypoint paths, interface implementations, override relationships, type/reference neighbors, and structurally similar nodes. Use after one issue is found to seed similar-bug-finder, semgrep-rule-creator, static-analysis, or manual review with graph-derived candidate locations.

Use it when:

- A finding is confirmed or plausible and variants may exist
- The vulnerable pattern depends on call context
- The issue involves a shared sink, source, validator, interface, override,
- The next step is to seed `similar-bug-finder`, `semgrep-rule-creator`,

Do not use it when:

- No seed issue exists. Use discovery or triage first.
- The pattern is purely syntactic and already obvious. Use
- The question is exploit-chain composition across multiple findings. Use a
- The goal is remediation verification. Use a remediation-review workflow.
- The seed cannot be bound to a graph node.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md on this repository. Write the result and the evidence to ./reports/codegraph-variant-neighborhood.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md` | Expands one confirmed or suspected vulnerability into a Codegraph graph neighborhood of variant candidates by finding sibling functions, shared callers and callees, common sensitive sinks, common entrypoint paths, interface... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/references/neighborhood-patterns.md` | Neighborhood Patterns: Use multiple bounded graph dimensions. Each dimension creates candidate review | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/references/neighborhood-patterns.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/references/output-format.md` | Output Format: Use Markdown unless the user asks for JSON. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/references/output-format.md before you start." |
| `plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/references/ranking.md` | Ranking: Rank candidates by review value, not by confirmed severity. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/codegraph-variant-neighborhood/references/ranking.md before you start." |

##### Skill: crypto-protocol-diagram

Entry point: `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md`

Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when diagramming a crypto protocol, visualizing a handshake or key exchange flow, extracting message flow from a spec or RFC, diagramming a ProVerif or Tamarin model, or drawing sequence diagrams for TLS, Noise, Signal, X3DH, Double Ratchet, FROST, DH, or ECDH protocols.

Use it when:

- User asks to diagram, visualize, or extract a cryptographic protocol
- Input is source code implementing a handshake, key exchange, or multi-party protocol
- Input is an RFC, academic paper, pseudocode, or formal model (ProVerif/Tamarin)
- User names a specific protocol (TLS, Noise, Signal, X3DH, FROST)

Do not use it when:

- User wants a call graph, class hierarchy, or module dependency map - use `diagramming-code`
- User wants to formally verify a protocol - use `mermaid-to-proverif` (after generating the diagram)
- Input has no cryptographic protocol semantics (no parties, no message exchange)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md on this repository. Write the result and the evidence to ./reports/crypto-protocol-diagram.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md` | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with cryptographic annotations. Use when... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/examples/simple-handshake/expected-output.md` | Expected Skill Output: This file shows what the crypto-protocol-diagram skill should produce when | Template or example. Say: "Use plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/examples/simple-handshake/expected-output.md as the format for the output." |
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/examples/simple-proverif/expected-output.md` | Expected Output: simple-proverif: This is the exact ASCII diagram and Mermaid file the crypto-protocol-diagram | Template or example. Say: "Use plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/examples/simple-proverif/expected-output.md as the format for the output." |
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/ascii-sequence-diagram.md` | ASCII Sequence Diagram Reference: Rules for drawing ASCII sequence diagrams inline in responses. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/ascii-sequence-diagram.md before you start." |
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/mermaid-sequence-syntax.md` | Mermaid Sequence Diagram Syntax Reference: Every sequence diagram starts with sequenceDiagram on its own line (no | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/mermaid-sequence-syntax.md before you start." |
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/protocol-patterns.md` | Crypto Protocol Patterns Reference: Canonical message flows for common cryptographic protocols. Use these as a | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/protocol-patterns.md before you start." |
| `plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/spec-parsing-patterns.md` | Spec Parsing Patterns Reference: Extraction rules for turning protocol specifications into sequence diagram | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/crypto-protocol-diagram/references/spec-parsing-patterns.md before you start." |

##### Skill: diagramming-code

Entry point: `plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md`

Generates Mermaid diagrams from Codegraph code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow visualizations. Use when visualizing code architecture, drawing call graphs, generating class diagrams, creating dependency maps, producing complexity heatmaps, or visualizing data flow and attack surface paths as Mermaid diagrams.

Use it when:

- Visualizing call paths between functions
- Drawing class inheritance hierarchies
- Mapping module import dependencies
- Showing class structure with members
- Highlighting complexity hotspots with color coding
- Tracing data flow from entrypoints to sensitive functions

Do not use it when:

- Querying the graph without visualization (use the `codegraph` skill)
- Mutation testing triage (use the `mutation-triage` skill)
- Architecture diagrams not derived from code (draw by hand)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md on this repository. Write the result and the evidence to ./reports/diagramming-code.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md` | Generates Mermaid diagrams from Codegraph code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow visualizations. Use when... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/diagramming-code/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/diagramming-code/references/diagram-types.md` | Diagram Types: Shows which functions call which. Built from callers_of / callees_of | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/diagramming-code/references/diagram-types.md before you start." |
| `plugins/code-auditing/codegraph/skills/diagramming-code/references/mermaid-syntax.md` | Mermaid Syntax Reference: Pitfalls and edge cases when generating Mermaid from code graph data. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/diagramming-code/references/mermaid-syntax.md before you start." |

##### Skill: graph-evolution

Entry point: `plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md`

Compares Codegraph code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint propagation changes, and privilege boundary modifications that text diffs miss. Use when comparing code between commits or tags, analyzing structural evolution, detecting attack surface growth, reviewing what changed between audit snapshots, or finding security-relevant changes that text diffs miss.

Use it when:

- Comparing two git refs to understand what structurally changed
- Auditing a range of commits for security-relevant evolution
- Detecting new attack paths created by code changes
- Finding functions whose blast radius or complexity grew silently
- Identifying taint propagation changes across refactors
- Pre-release structural comparison (tag-to-tag or branch-to-branch)

Do not use it when:

- Line-level code review (use `differential-review` for text-diff analysis)
- Single-snapshot analysis (use the `codegraph` skill directly)
- Diagram generation from a single snapshot (use the `diagramming-code` skill)
- Mutation testing triage (use the `mutation-triage` skill)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md on this repository. Write the result and the evidence to ./reports/graph-evolution.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md` | Compares Codegraph code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast radius growth, taint... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/graph-evolution/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/graph-evolution/references/evolution-metrics.md` | Evolution Metrics Reference: This document explains each structural metric the graph-evolution skill | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/graph-evolution/references/evolution-metrics.md before you start." |
| `plugins/code-auditing/codegraph/skills/graph-evolution/references/report-format.md` | Report Format Reference: Output format for graph-evolution reports. The report is a markdown file | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/graph-evolution/references/report-format.md before you start." |

##### Skill: mermaid-to-proverif

Entry point: `plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md`

Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to ProVerif, verifying protocol security properties (secrecy, authentication, forward secrecy), checking for replay attacks, or producing a .pv file from a sequence diagram.

Use it when:

- User asks to formally verify a cryptographic protocol described as a Mermaid sequenceDiagram
- User wants to generate a ProVerif model (.pv file) from a protocol diagram
- User wants to prove secrecy, authentication, or forward secrecy properties
- Input is the output of the `crypto-protocol-diagram` skill

Do not use it when:

- No Mermaid sequenceDiagram exists yet - use `crypto-protocol-diagram` first to generate one
- User wants to verify properties of non-cryptographic systems (state machines, access control)
- User wants to run ProVerif on an existing .pv file - just run `proverif model.pv` directly

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md on this repository. Write the result and the evidence to ./reports/mermaid-to-proverif.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md` | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol, converting a Mermaid diagram to... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/mermaid-to-proverif/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/mermaid-to-proverif/examples/simple-handshake/diagram.md` | Simple Authenticated Key Exchange Sequence Diagram: | Template or example. Say: "Use plugins/code-auditing/codegraph/skills/mermaid-to-proverif/examples/simple-handshake/diagram.md as the format for the output." |
| `plugins/code-auditing/codegraph/skills/mermaid-to-proverif/references/crypto-to-proverif-mapping.md` | Cryptographic Operation to ProVerif Mapping: Maps every Mermaid annotation produced by the crypto-protocol-diagram skill | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/mermaid-to-proverif/references/crypto-to-proverif-mapping.md before you start." |
| `plugins/code-auditing/codegraph/skills/mermaid-to-proverif/references/proverif-syntax.md` | ProVerif Syntax Reference: ProVerif models cryptographic protocols in the applied pi-calculus. This | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/mermaid-to-proverif/references/proverif-syntax.md before you start." |
| `plugins/code-auditing/codegraph/skills/mermaid-to-proverif/references/security-properties.md` | Security Properties in ProVerif: A guide to choosing and expressing the right security queries for a given | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/mermaid-to-proverif/references/security-properties.md before you start." |

##### Skill: mutation-triage

Entry point: `plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md`

Graph-informed mutation testing triage. Parses codebases with Codegraph, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing test coverage, and fuzzing targets. Use when triaging survived mutants, analyzing mutation testing results, identifying test gaps, finding fuzzing targets from weak tests, running mutation frameworks (including circom-mutator and cairo-mutator), or using necessist.

Use it when:

- After mutation testing reveals survived mutants that need triage
- Identifying where unit tests would have the highest impact
- Finding functions that need fuzz harnesses instead of unit tests
- Prioritizing test improvements using data flow context
- Filtering out harmless mutants from actionable ones
- Finding unnecessary test statements that indicate weak assertions (necessist)

Do not use it when:

- Codebase has no existing test suite (write tests first)
- Pure documentation or configuration changes
- Single-file scripts with trivial logic

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md on this repository. Write the result and the evidence to ./reports/mutation-triage.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md` | Graph-informed mutation testing triage. Parses codebases with Codegraph, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify false positives, missing... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/mutation-triage/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/mutation-triage/references/graph-analysis.md` | Graph Analysis for Mutant Triage: How to use codegraph's code graph data to contextualize survived mutants | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/mutation-triage/references/graph-analysis.md before you start." |
| `plugins/code-auditing/codegraph/skills/mutation-triage/references/mutation-frameworks.md` | Mutation Testing Frameworks: Language-specific setup, execution, and output parsing for mutation testing. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/mutation-triage/references/mutation-frameworks.md before you start." |
| `plugins/code-auditing/codegraph/skills/mutation-triage/references/triage-methodology.md` | Triage Methodology: Detailed criteria for classifying survived mutants into actionable buckets. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/mutation-triage/references/triage-methodology.md before you start." |

##### Skill: slicing-code-context

Entry point: `plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md`

Selects bounded, graph-informed source slices with Codegraph and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading function-, class-, caller-, callee-, call-path-, entrypoint-, or line-focused code tasks to constrained or locally hosted models without exposing the full repository.

Use it when:

- Offload explanation, classification, review, or mechanical edit proposals for a function or class
- Trace callers, callees, shortest call paths, or entrypoint-to-target paths within a small context window
- Focus a local or lower-cost model on explicit source lines and their graph neighborhood
- Keep repository access and final judgment with the coordinator

Do not use it when:

- The worker must explore the repository or discover its own scope
- Runtime behavior, generated code, macros, or dynamic dispatch dominate what Codegraph can see
- The anchor alone cannot fit and no meaningful line range is known
- The task requires direct worker edits; workers may only propose changes
- A small file can be read safely without graph selection or delegation

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md on this repository. Write the result and the evidence to ./reports/slicing-code-context.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md` | Selects bounded, graph-informed source slices with Codegraph and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading function-, class-, caller-, callee-, call-path-, entrypoint-,... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/slicing-code-context/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/slicing-code-context/references/slice-packet.md` | Slice Packet and Worker Contract: The slicer emits schema version 1.0 as JSON or Markdown. JSON is the preferred | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/slicing-code-context/references/slice-packet.md before you start." |

##### Skill: vector-forge

Entry point: `plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md`

Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the uncovered code paths. Compares before/after mutation kill rates to prove vector effectiveness. Use when generating cryptographic test vectors, measuring Wycheproof coverage gaps, finding escaped mutants via mutation testing, creating cross-implementation test suites, or improving test vector coverage for crypto primitives.

Use it when:

- Generating test vectors for cryptographic algorithms or protocols
- Evaluating how well existing test vectors cover an implementation
- Finding implementation code paths that no test vector exercises
- Creating Wycheproof-style cross-implementation test vectors
- Measuring the concrete coverage value of a test vector suite

Do not use it when:

- No implementations exist yet (need code to mutate)
- Single trivial implementation with no edge cases
- Testing application logic rather than algorithm implementations
- The algorithm has no public test vectors to compare against

Requests you can copy:

- **Use:** `Use plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md on this repository. Write the result and the evidence to ./reports/vector-forge.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md` | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliberately exercise the... | Start here. Say: "Follow plugins/code-auditing/codegraph/skills/vector-forge/SKILL.md on this repository." |
| `plugins/code-auditing/codegraph/skills/vector-forge/references/fault-simulation.md` | Fault Simulation via Limb-Width Reimplementation: Generate test vectors that catch carry propagation, modular | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/vector-forge/references/fault-simulation.md before you start." |
| `plugins/code-auditing/codegraph/skills/vector-forge/references/lessons-learned.md` | Lessons Learned (BLS12-381 Case Study): Patterns observed during mutation testing of gnark-crypto (Go), | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/vector-forge/references/lessons-learned.md before you start." |
| `plugins/code-auditing/codegraph/skills/vector-forge/references/mutation-frameworks.md` | Mutation Testing Frameworks: Language-specific setup, execution, and output parsing for mutation testing. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/vector-forge/references/mutation-frameworks.md before you start." |
| `plugins/code-auditing/codegraph/skills/vector-forge/references/report-template.md` | Vector Forge Report Template: Write the report to VECTOR_FORGE_REPORT.md in the working directory. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/vector-forge/references/report-template.md before you start." |
| `plugins/code-auditing/codegraph/skills/vector-forge/references/vector-patterns.md` | Test Vector Patterns for Cryptographic Primitives: Patterns for designing test vectors that target specific code paths | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/code-auditing/codegraph/skills/vector-forge/references/vector-patterns.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/codegraph/agents/code-slice-worker.md` | Analyzes one bounded Codegraph source packet and returns source-cited JSON without accessing the repository. Use only when invoked by the slicing-code-context coordinator. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/codegraph/agents/code-slice-worker.md." |
| `plugins/code-auditing/codegraph/README.md` | codegraph: Source code graph analysis for security auditing. Parses code into queryable graphs of functions, classes, and calls, then uses that structure for diagram generation, mutation testing triage, protocol verification,... | Human documentation. Read it for install notes and extra details. |

#### testing-skills

Folder: [plugins/code-auditing/testing-skills/](plugins/code-auditing/testing-skills/)  |  [README](plugins/code-auditing/testing-skills/README.md)  |  [AGENTS.md](plugins/code-auditing/testing-skills/AGENTS.md)

Skills from the Aevrin Security Application Security Testing Guide (aevrin.net)

##### Skill: address-sanitizer

Entry point: `plugins/code-auditing/testing-skills/skills/address-sanitizer/SKILL.md`

Builds and runs code under AddressSanitizer to catch buffer overflows, use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=address builds, ASAN_OPTIONS, reading the crash report, LeakSanitizer, and the overhead and platform trade-offs. Use when fuzzing C/C++ or Rust that has unsafe blocks or FFI, when debugging a memory corruption crash, or when reading an ASan stack trace.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/address-sanitizer/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/address-sanitizer/SKILL.md on this repository. Write the result and the evidence to ./reports/address-sanitizer.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/address-sanitizer/SKILL.md` | Builds and runs code under AddressSanitizer to catch buffer overflows, use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=address builds, ASAN_OPTIONS, reading the crash report, LeakSanitizer,... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/address-sanitizer/SKILL.md on this repository." |

##### Skill: aflpp

Entry point: `plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md`

Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode, corpus minimization, and crash triage. Use when scaling fuzzing across cores, fuzzing a mature C/C++ codebase, reading the afl-fuzz status screen, or moving on after libFuzzer has plateaued.

Use it when:

- You need multi-core fuzzing to maximize throughput
- Your project can be compiled with Clang or GCC
- You want diverse mutation strategies and mature tooling
- libFuzzer has plateaued and you need more coverage
- You're fuzzing production codebases that benefit from parallel execution

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md on this repository. Write the result and the evidence to ./reports/aflpp.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md` | Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode, corpus minimization, and crash... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/aflpp/SKILL.md on this repository." |

##### Skill: atheris

Entry point: `plugins/code-auditing/testing-skills/skills/atheris/SKILL.md`

Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and native C extensions, and running under AddressSanitizer. Use when fuzzing a Python package, hunting memory corruption in a Python C extension, or choosing between Atheris and Hypothesis for a Python target.

Use it when:

- Fuzzing pure Python code with coverage guidance
- Testing Python C extensions for memory corruption
- Integration with libFuzzer ecosystem is desired
- AddressSanitizer support is needed

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/atheris/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/atheris/SKILL.md on this repository. Write the result and the evidence to ./reports/atheris.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/atheris/SKILL.md` | Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and native C extensions, and running under AddressSanitizer. Use... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/atheris/SKILL.md on this repository." |
| `plugins/code-auditing/testing-skills/skills/atheris/examples.md` | Atheris Examples: Two complete harnesses, each runnable as written. | Guide loaded during the work. Say: "Read plugins/code-auditing/testing-skills/skills/atheris/examples.md before you start." |
| `plugins/code-auditing/testing-skills/skills/atheris/structured-input.md` | Structured Input with FuzzedDataProvider: A target that takes several typed arguments - a string, a length, a flag - wastes most of | Guide loaded during the work. Say: "Read plugins/code-auditing/testing-skills/skills/atheris/structured-input.md before you start." |

##### Skill: cargo-fuzz

Entry point: `plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md`

Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses, Arbitrary-derived structured inputs, sanitizer options, cargo fuzz coverage, and reproducing a crash artifact. Use when fuzzing a Rust crate, writing a fuzz_target!, exercising unsafe blocks or FFI in Rust, or triaging a cargo fuzz crash.

Use it when:

- Your project uses Cargo (required)
- You want simple, quick setup with minimal configuration
- You need integrated sanitizer support
- You're fuzzing Rust code with or without unsafe blocks

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md on this repository. Write the result and the evidence to ./reports/cargo-fuzz.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md` | Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses, Arbitrary-derived structured inputs, sanitizer options,... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/cargo-fuzz/SKILL.md on this repository." |

##### Skill: constant-time-testing

Entry point: `plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md`

Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing. Covers the formal, symbolic, dynamic, and statistical tool categories and how to read a result. Use when testing whether a running implementation is constant-time, measuring timing variance on a compiled binary, or investigating a suspected timing attack. Not for statically inspecting compiler output - the constant-time-analysis plugin covers that.

Use it when:

- Auditing cryptographic implementations (primitives, protocols)
- Code handles secret keys, passwords, or sensitive cryptographic material
- Implementing crypto algorithms from scratch
- Reviewing PRs that touch crypto code
- Investigating potential timing vulnerabilities
- Code does not process secret data
- Public algorithms with no secret inputs

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md on this repository. Write the result and the evidence to ./reports/constant-time-testing.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md` | Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing. Covers the formal, symbolic, dynamic, and statistical tool... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/constant-time-testing/SKILL.md on this repository." |

##### Skill: coverage-analysis

Entry point: `plugins/code-auditing/testing-skills/skills/coverage-analysis/SKILL.md`

Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. Covers baselining a new campaign, reading coverage reports, and turning uncovered regions into harness, seed, or dictionary work. Use when a fuzzer plateaus, when judging whether a harness is effective, after changing a harness, or when asking why some code is never reached.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/coverage-analysis/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/coverage-analysis/SKILL.md on this repository. Write the result and the evidence to ./reports/coverage-analysis.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/coverage-analysis/SKILL.md` | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. Covers baselining a new campaign, reading coverage reports, and turning uncovered regions into harness,... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/coverage-analysis/SKILL.md on this repository." |

##### Skill: fuzzing-dictionary

Entry point: `plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md`

Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers, binaries, and specifications, dictionary syntax, and wiring one into libFuzzer or AFL++. Use when fuzzing a parser, protocol, or file format, when coverage stalls at input validation, or when a target compares against fixed strings.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md on this repository. Write the result and the evidence to ./reports/fuzzing-dictionary.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md` | Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers, binaries, and specifications, dictionary syntax, and wiring... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/fuzzing-dictionary/SKILL.md on this repository." |

##### Skill: fuzzing-obstacles

Entry point: `plugins/code-auditing/testing-skills/skills/fuzzing-obstacles/SKILL.md`

Patches past the barriers that stop a fuzzer making progress - checksum and hash verification, magic-value validation, time-based seeds, and other non-deterministic global state. Covers locating the blocking check, neutering it behind a fuzzing build flag, and avoiding the false positives a patch can introduce. Use when a fuzzer is stuck at validation, when coverage shows large regions behind a checksum, or when valid inputs are impractical to generate.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/fuzzing-obstacles/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/fuzzing-obstacles/SKILL.md on this repository. Write the result and the evidence to ./reports/fuzzing-obstacles.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/fuzzing-obstacles/SKILL.md` | Patches past the barriers that stop a fuzzer making progress - checksum and hash verification, magic-value validation, time-based seeds, and other non-deterministic global state. Covers locating the blocking check, neutering... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/fuzzing-obstacles/SKILL.md on this repository." |

##### Skill: harness-writing

Entry point: `plugins/code-auditing/testing-skills/skills/harness-writing/SKILL.md`

Designs and improves fuzzing harnesses for C/C++ and Rust. Covers mapping raw bytes onto a target API, generating structured inputs, avoiding non-determinism and false crashes, and deciding what to fuzz together. Use when writing a first LLVMFuzzerTestOneInput or fuzz_target! harness, when a campaign finds nothing or reports crashes that will not reproduce, or when the target API needs structured rather than raw input.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/harness-writing/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/harness-writing/SKILL.md on this repository. Write the result and the evidence to ./reports/harness-writing.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/harness-writing/SKILL.md` | Designs and improves fuzzing harnesses for C/C++ and Rust. Covers mapping raw bytes onto a target API, generating structured inputs, avoiding non-determinism and false crashes, and deciding what to fuzz together. Use when... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/harness-writing/SKILL.md on this repository." |

##### Skill: libafl

Entry point: `plugins/code-auditing/testing-skills/skills/libafl/SKILL.md`

Builds custom fuzzers with LibAFL, the modular Rust fuzzing library. Covers composing observers, feedbacks, mutators, schedulers, and executors into a fuzzer for targets the standard tools do not fit. Use when writing a bespoke fuzzer or mutator, fuzzing a non-standard target or architecture, implementing a fuzzing research idea, or when libFuzzer and AFL++ lack the control you need.

Use it when:

- You need custom mutation strategies or feedback mechanisms
- Standard fuzzers don't support your target architecture
- You want to implement novel fuzzing techniques
- You need fine-grained control over fuzzing components
- You're conducting fuzzing research

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/libafl/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/libafl/SKILL.md on this repository. Write the result and the evidence to ./reports/libafl.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/libafl/SKILL.md` | Builds custom fuzzers with LibAFL, the modular Rust fuzzing library. Covers composing observers, feedbacks, mutators, schedulers, and executors into a fuzzer for targets the standard tools do not fit. Use when writing a... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/libafl/SKILL.md on this repository." |

##### Skill: libfuzzer

Entry point: `plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md`

Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds, corpus and dictionary management, sanitizer integration, and campaign triage. Use when writing or debugging an LLVMFuzzerTestOneInput harness, starting fuzzing on a C/C++ library, choosing between libFuzzer and AFL++, or working out why a libFuzzer run finds nothing.

Use it when:

- You need a simple, quick setup for C/C++ code
- Project uses Clang for compilation
- Single-core fuzzing is sufficient initially
- Transitioning to AFL++ later is an option (harnesses are compatible)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md on this repository. Write the result and the evidence to ./reports/libfuzzer.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md` | Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds, corpus and dictionary management, sanitizer integration, and... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/libfuzzer/SKILL.md on this repository." |

##### Skill: ossfuzz

Entry point: `plugins/code-auditing/testing-skills/skills/ossfuzz/SKILL.md`

Enrolls a project in OSS-Fuzz, Google's free continuous fuzzing service for open source, and drives it locally. Covers project.yaml, Dockerfile and build.sh setup, the helper scripts, reproducing OSS-Fuzz crash reports, and the acceptance criteria. Use when setting up continuous fuzzing for an open-source project, reproducing an OSS-Fuzz bug report, or testing an OSS-Fuzz build before submitting it.

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/ossfuzz/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/ossfuzz/SKILL.md on this repository. Write the result and the evidence to ./reports/ossfuzz.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/ossfuzz/SKILL.md` | Enrolls a project in OSS-Fuzz, Google's free continuous fuzzing service for open source, and drives it locally. Covers project.yaml, Dockerfile and build.sh setup, the helper scripts, reproducing OSS-Fuzz crash reports, and... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/ossfuzz/SKILL.md on this repository." |

##### Skill: rubyfuzz

Entry point: `plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md`

Sets up and runs Rubyfuzz, a coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and the native C extensions in gems, and sanitizer builds. Use when fuzzing a Ruby library or gem, testing a Ruby C extension for memory safety, or asking how to fuzz Ruby at all.

Use it when:

- Fuzzing Ruby applications or libraries
- Testing Ruby C extensions for memory safety issues
- You need coverage-guided fuzzing for Ruby code
- Working with Ruby gems that have native extensions

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md on this repository. Write the result and the evidence to ./reports/rubyfuzz.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md` | Sets up and runs Rubyfuzz, a coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and the native C extensions in gems, and sanitizer builds. Use when... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/rubyfuzz/SKILL.md on this repository." |

##### Skill: testing-guide-generator

Entry point: `plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md`

Generates agent skills from the Aevrin Security Testing Guide (aevrin.net), analyzing guide pages and emitting SKILL.md files with the structure each skill type requires. Use when creating or refreshing a skill from guide content, or when the user names the testing guide or aevrin.net. Not for answering security testing questions - the generated skills cover those.

Use it when:

- Creating new security testing skills from guide content
- User mentions "testing guide", "aevrin.net", or asks about generating skills
- Bulk skill generation or refresh is needed
- General security testing questions (use the generated skills)
- Non-guide skill creation

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md on this repository. Write the result and the evidence to ./reports/testing-guide-generator.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md` | Generates agent skills from the Aevrin Security Testing Guide (aevrin.net), analyzing guide pages and emitting SKILL.md files with the structure each skill type requires. Use when creating or refreshing a skill from guide... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/testing-guide-generator/SKILL.md on this repository." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/agent-prompt.md` | Agent Prompt Template: Use this prompt when spawning each skill generation agent. Variables in {braces} are substituted from the per-skill package (see [discovery.md](discovery.md#phase-3-prepare-generation-context)). | Guide loaded during the work. Say: "Read plugins/code-auditing/testing-skills/skills/testing-guide-generator/agent-prompt.md before you start." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/discovery.md` | Discovery Workflow: Methodology for analyzing the Testing Guide and identifying skill candidates. | Guide loaded during the work. Say: "Read plugins/code-auditing/testing-skills/skills/testing-guide-generator/discovery.md before you start." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/domain-skill.md` | Domain Skill Template: Use this template for domain-specific security testing (cryptographic testing, web security methodologies, etc.). | Template or example. Say: "Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/domain-skill.md as the format for the output." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/fuzzer-skill.md` | Fuzzer Skill Template: Use this template for language-specific fuzzers (libFuzzer, AFL++, cargo-fuzz, etc.). | Template or example. Say: "Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/fuzzer-skill.md as the format for the output." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/technique-skill.md` | Technique Skill Template: Use this template for cross-cutting techniques that apply to multiple tools (harness writing, coverage analysis, sanitizers, dictionaries, etc.). | Template or example. Say: "Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/technique-skill.md as the format for the output." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/tool-skill.md` | Tool Skill Template: Use this template for static analysis tools (Semgrep, CodeQL) and similar standalone CLI tools. | Template or example. Say: "Use plugins/code-auditing/testing-skills/skills/testing-guide-generator/templates/tool-skill.md as the format for the output." |
| `plugins/code-auditing/testing-skills/skills/testing-guide-generator/testing.md` | Testing Strategy: Methodology for validating generated skills. | Guide loaded during the work. Say: "Read plugins/code-auditing/testing-skills/skills/testing-guide-generator/testing.md before you start." |

##### Skill: wycheproof

Entry point: `plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md`

Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more. Covers loading test vectors, mapping result flags onto pass and fail expectations, and reading a failure. Use when testing a crypto implementation against known attacks, checking a library against standard test vectors, or investigating why two implementations disagree on the same input.

Use it when:

- Testing cryptographic implementations (AES-GCM, ECDSA, ECDH, RSA, etc.)
- Validating that crypto code handles edge cases correctly
- Verifying implementations against known attack vectors
- Setting up CI/CD for cryptographic libraries
- Auditing third-party crypto code for correctness
- Testing for timing side-channels (use constant-time testing tools instead)
- Finding new unknown bugs (use fuzzing instead)

Requests you can copy:

- **Use:** `Use plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md on this repository. Write the result and the evidence to ./reports/wycheproof.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md` | Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more. Covers loading test vectors, mapping result flags onto pass... | Start here. Say: "Follow plugins/code-auditing/testing-skills/skills/wycheproof/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/code-auditing/testing-skills/README.md` | Testing Guide Skills: Meta-skill that generates agent skills from the [Aevrin Security Application Security Testing Guide](https://aevrin.net). | Human documentation. Read it for install notes and extra details. |

### Malware Analysis

#### yara-authoring

Folder: [plugins/malware-analysis/yara-authoring/](plugins/malware-analysis/yara-authoring/)  |  [README](plugins/malware-analysis/yara-authoring/README.md)  |  [AGENTS.md](plugins/malware-analysis/yara-authoring/AGENTS.md)

YARA-X detection rule authoring with linting and quality analysis

##### Skill: yara-rule-authoring

Entry point: `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/SKILL.md`

Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conventions, string selection, performance optimization, migration from legacy YARA, and false positive reduction. Triggers on: YARA, YARA-X, malware detection, threat hunting, IOC, signature, crx module, dex module.

Use it when:

- Writing new YARA-X rules for malware detection
- Reviewing existing rules for quality or performance issues
- Optimizing slow-running rulesets
- Converting IOCs or threat intel into detection signatures
- Debugging false positive issues
- Preparing rules for production deployment
- Migrating legacy YARA rules to YARA-X

Do not use it when:

- Static analysis requiring disassembly → use Ghidra/IDA skills
- Dynamic malware analysis → use sandbox analysis skills
- Network-based detection → use Suricata/Snort skills
- Memory forensics with Volatility → use memory forensics skills
- Simple hash-based detection → just use hash lists

Requests you can copy:

- **Use:** `Use plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/SKILL.md on this repository. Write the result and the evidence to ./reports/yara-rule-authoring.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/SKILL.md` | Guides authoring of high-quality YARA-X detection rules for malware identification. Use when writing, reviewing, or optimizing YARA rules. Covers naming conventions, string selection, performance optimization, migration from... | Start here. Say: "Follow plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/SKILL.md on this repository." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/crx-module.md` | YARA-X CRX Module Reference: The crx module enables analysis of Chrome extension packages (CRX files). Use it to detect malicious extensions based on their declared permissions, manifest structure, and metadata. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/crx-module.md before you start." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/dex-module.md` | YARA-X DEX Module Reference: The dex module enables analysis of Android Dalvik Executable (DEX) files. Use it to detect Android malware based on class structure, method signatures, string content, and obfuscation patterns. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/dex-module.md before you start." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/performance.md` | YARA-X Performance Guidelines: Understanding how YARA-X works internally helps you write rules that scan fast. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/performance.md before you start." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/strings.md` | YARA-X String Selection: Choosing the right strings is the most critical decision in YARA rule writing. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/strings.md before you start." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/style-guide.md` | YARA Naming and Metadata: Consistent naming for maintainable rule sets. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/style-guide.md before you start." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/testing.md` | YARA-X Rule Testing: Testing is non-negotiable. Untested rules cause alert fatigue (false positives) or missed detections (false negatives). | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/references/testing.md before you start." |
| `plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/workflows/rule-development.md` | YARA Rule Development Workflow: This guide walks through the complete process of developing a production-quality YARA-X rule, from sample collection to deployment. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/malware-analysis/yara-authoring/skills/yara-rule-authoring/workflows/rule-development.md and run that phase." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/malware-analysis/yara-authoring/README.md` | YARA-X Authoring Plugin: A behavior-driven skill for authoring high-quality YARA-X detection rules, teaching you to think and act like an expert YARA author. | Human documentation. Read it for install notes and extra details. |

### Verification

#### constant-time-analysis

Folder: [plugins/verification/constant-time-analysis/](plugins/verification/constant-time-analysis/)  |  [README](plugins/verification/constant-time-analysis/README.md)  |  [AGENTS.md](plugins/verification/constant-time-analysis/AGENTS.md)

Detect compiler-induced timing side-channels in cryptographic code

##### Skill: constant-time-analysis

Entry point: `plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md`

Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++, Go, Rust, Swift, Java, Kotlin, C#, PHP, JavaScript, TypeScript, Python, or Ruby.

Use it when:

- Implementing or reviewing a signature, encryption, KEM, or key derivation routine
- Code applies `/` or `%` to a value derived from a key, plaintext, nonce, or token
- The user mentions "constant-time", "timing attack", "side-channel", or "KyberSlash"
- Reviewing functions named `sign`, `verify`, `encrypt`, `decrypt`, `derive_key`

Do not use it when:

- **Measuring** timing variance on a running binary - use the `constant-time-testing` skill from the `testing-skills` plugin, which covers dudect and statistical approaches and may not be installed. This skill inspects compiler output statically and never executes the code under test.
- Non-cryptographic code, or crypto code where every input is public
- High-level API usage where a vetted library owns the constant-time guarantees
- Cache and other microarchitectural side channels - the assembly view cannot see them

Requests you can copy:

- **Find:** `Use plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md. Scan the cryptographic code in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md. Scan the cryptographic code in ./src. Write a detailed report to ./reports/constant-time-analysis.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/constant-time-analysis.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md` | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time programming questions in C, C++,... | Start here. Say: "Follow plugins/verification/constant-time-analysis/skills/constant-time-analysis/SKILL.md on the cryptographic code in ./src." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/README.md` | Constant-Time Analysis Skill: A Claude Code skill that detects timing side-channel vulnerabilities in cryptographic code by analyzing assembly or bytecode output for dangerous instructions. | Human documentation. Read it for install notes and extra details. |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/compiled.md` | Constant-Time Analysis: Compiled Languages: Analysis guidance for C, C++, Go, and Rust. These languages compile to native assembly, where timing side-channels are detected by scanning for variable-time CPU instructions. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/compiled.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/javascript.md` | Constant-Time Analysis: JavaScript and TypeScript: Analysis guidance for JavaScript and TypeScript. Uses V8 bytecode output from Node.js to detect timing-unsafe operations. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/javascript.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/kotlin.md` | Constant-Time Analysis: Kotlin: Analysis guidance for Kotlin targeting Android and JVM platforms. Kotlin compiles to JVM bytecode, sharing the same runtime characteristics as Java. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/kotlin.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/php.md` | Constant-Time Analysis: PHP: Analysis guidance for PHP scripts. Uses the VLD extension or OPcache debug output to analyze Zend opcodes. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/php.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/python.md` | Constant-Time Analysis: Python: Analysis guidance for Python scripts. Uses the dis module to analyze CPython bytecode for timing-unsafe operations. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/python.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/ruby.md` | Constant-Time Analysis: Ruby: Analysis guidance for Ruby scripts. Uses YARV (Yet Another Ruby VM) instruction sequence dump to analyze bytecode for timing-unsafe operations. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/ruby.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/swift.md` | Constant-Time Analysis: Swift: Analysis guidance for Swift targeting iOS, macOS, watchOS, and tvOS. Swift compiles to native code, making it subject to the same CPU-level timing side-channels as C, C++, Go, and Rust. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/swift.md before you start." |
| `plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/vm-compiled.md` | Constant-Time Analysis: VM-Compiled Languages: Analysis guidance for Java and C#. These languages compile to bytecode (JVM bytecode / CIL) that runs on a virtual machine with Just-In-Time (JIT) compilation to native code. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/constant-time-analysis/skills/constant-time-analysis/references/vm-compiled.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/constant-time-analysis/commands/ct-check.md` | Detects timing side-channels in cryptographic code | Saved prompt. Say: "Follow plugins/verification/constant-time-analysis/commands/ct-check.md on the cryptographic code in ./src." |
| `plugins/verification/constant-time-analysis/README.md` | Constant-Time Analyzer (ct-analyzer): A portable tool for detecting timing side-channel vulnerabilities in compiled cryptographic code. Analyzes assembly output from multiple compilers and architectures to detect instructions... | Human documentation. Read it for install notes and extra details. |

#### post-patch-validation

Folder: [plugins/verification/post-patch-validation/](plugins/verification/post-patch-validation/)  |  [README](plugins/verification/post-patch-validation/README.md)  |  [AGENTS.md](plugins/verification/post-patch-validation/AGENTS.md)

Validates security patches against the reported bug, root-cause variants, and surrounding behavior. Returns reproducible failures to repair and validation gaps, with pinned inputs and saved evidence. Bundles a validate-patch dynamic workflow for Claude Code.

##### Skill: post-patch-validation

Entry point: `plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md`

Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. Use after a patch exists and before accepting, merging, or reporting it as fixed; also use when an AI-generated patch, remediation commit, pull request, or proposed upstream fix needs adversarial post-patch validation across any language.

Use it when:

- A security fix, remediation commit, patch file, or pull request already exists.
- An AI-generated patch needs validation before human review or merge.
- A fix may cover one exploit path while missing variants of the same root cause.
- A security fix may alter legitimate behavior or introduce a new vulnerability.
- A patch author needs concrete failures and coverage gaps before another revision.

Do not use it when:

- No patch exists yet; use vulnerability discovery or fix implementation first.
- The task is to review an audit finding against a report without executing patch evidence.
- The task is only to convert a finding into a permanent project test.
- The target is remote or production. This skill executes local code and tests only.
- The user has not authorized execution of the repository's code or test suite.

Requests you can copy:

- **Check:** `Use plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.`
- **Report:** `Use plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/post-patch-validation.md with the verdict and the evidence for it.`
- **Fix:** `Read ./reports/post-patch-validation.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md` | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, root-cause variants, behavior preservation, regressions, and newly introduced security failures. Use after a patch... | Start here. Say: "Follow plugins/verification/post-patch-validation/skills/post-patch-validation/SKILL.md on this repository." |
| `plugins/verification/post-patch-validation/skills/post-patch-validation/references/evidence-model.md` | Evidence Model: Use this reference while authoring the validation plan or interpreting its result. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/post-patch-validation/skills/post-patch-validation/references/evidence-model.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/post-patch-validation/README.md` | Post-Patch Validation: Validate a security patch against the reported bug and the surrounding code it affects. Give the | Human documentation. Read it for install notes and extra details. |

#### property-based-testing

Folder: [plugins/verification/property-based-testing/](plugins/verification/property-based-testing/)  |  [README](plugins/verification/property-based-testing/README.md)  |  [AGENTS.md](plugins/verification/property-based-testing/AGENTS.md)

Write, review, and triage property-based tests - Hypothesis, fast-check, proptest, and Echidna or Medusa for Solidity invariants

##### Skill: property-based-testing

Entry point: `plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md`

Writes, reviews, and debugs property-based tests - Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input domain instead of a hand-picked list of examples: encode/decode and serialize/deserialize pairs, parsers, canonicalizers and normalizers, validators, numeric and Decimal types, comparators and sort order, data structures, and smart-contract state invariants. Also use when adding cases to an existing @given, fast-check, or proptest suite, when judging whether existing property tests assert anything real, and when a generator has shrunk a counterexample and you need to tell a wrong property from a genuine bug. Not for coverage-guided binary fuzzing (libFuzzer, AFL), mutation-testing campaigns, static analysis, benchmarking, or end-to-end UI tests.

Requests you can copy:

- **Check:** `Use plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.`
- **Report:** `Use plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/property-based-testing.md with the verdict and the evidence for it.`
- **Fix:** `Read ./reports/property-based-testing.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md` | Writes, reviews, and debugs property-based tests - Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input domain instead of a hand-picked... | Start here. Say: "Follow plugins/verification/property-based-testing/skills/property-based-testing/SKILL.md on this repository." |
| `plugins/verification/property-based-testing/skills/property-based-testing/README.md` | Property-Based Testing Skill: Guidance for property-based testing across languages, including Echidna and Medusa for | Human documentation. Read it for install notes and extra details. |
| `plugins/verification/property-based-testing/skills/property-based-testing/references/generating.md` | Generating Property-Based Tests: Writing the @given decorator is the easy part. These are the decisions that make | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/property-based-testing/skills/property-based-testing/references/generating.md before you start." |
| `plugins/verification/property-based-testing/skills/property-based-testing/references/interpreting-failures.md` | Interpreting Property-Based Test Failures: A property test that fails has told you one of three things, and they need different | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/property-based-testing/skills/property-based-testing/references/interpreting-failures.md before you start." |
| `plugins/verification/property-based-testing/skills/property-based-testing/references/libraries.md` | PBT Libraries by Language: Match the project's existing choice. Introducing a second PBT library into a codebase | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/property-based-testing/skills/property-based-testing/references/libraries.md before you start." |
| `plugins/verification/property-based-testing/skills/property-based-testing/references/refactoring.md` | Refactoring to Expose a Property: "This code has no algebraic shape" is often a fact about how the code is *arranged* | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/property-based-testing/skills/property-based-testing/references/refactoring.md before you start." |
| `plugins/verification/property-based-testing/skills/property-based-testing/references/reviewing.md` | Reviewing Property-Based Tests: A property test can pass for years while asserting nothing. These are the ways that | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/property-based-testing/skills/property-based-testing/references/reviewing.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/property-based-testing/README.md` | Property-Based Testing: Write, review, and triage property-based tests - Hypothesis, fast-check, proptest, and | Human documentation. Read it for install notes and extra details. |

#### spec-to-code-compliance

Folder: [plugins/verification/spec-to-code-compliance/](plugins/verification/spec-to-code-compliance/)  |  [README](plugins/verification/spec-to-code-compliance/README.md)  |  [AGENTS.md](plugins/verification/spec-to-code-compliance/AGENTS.md)

Check code against the documentation that specifies it: one agent per requirement, divergences refuted before they are reported, evidence cited to the line

##### Skill: spec-to-code-compliance

Entry point: `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md`

Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. Use when comparing an implementation against a whitepaper, protocol spec, or design document.

Requests you can copy:

- **Find:** `Use plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md. Scan this repository and its specification. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md. Scan this repository and its specification. Write a detailed report to ./reports/spec-to-code-compliance.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/spec-to-code-compliance.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md` | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, which are absent, and what the code does that no document mentions. Use when comparing an implementation against a... | Start here. Say: "Follow plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md on this repository and its specification." |
| `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/ANALYSIS_FORMAT.md` | Analysis Format: The output format for a per-requirement analysis. The agent defines what to check; this defines how to write it | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/ANALYSIS_FORMAT.md before you start." |
| `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/DIVERGENCE_RUBRIC.md` | Divergence Rubric: Severity is about consequence, not about how far the code strayed from the words. A requirement the code | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/DIVERGENCE_RUBRIC.md before you start." |
| `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/DOMAIN_NOTES.md` | Domain Notes: The question never changes. For each requirement: what does it demand of an implementation, where would that be | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/DOMAIN_NOTES.md before you start." |
| `plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/WORKED_EXAMPLE.md` | Worked Examples: Three requirements against real code shapes, one per verdict that is easy to get wrong. Read these for | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/spec-to-code-compliance/skills/spec-to-code-compliance/resources/WORKED_EXAMPLE.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/spec-to-code-compliance/agents/spec-compliance-checker.md` | Checks one documented requirement against the code that should implement it, and returns a verdict with the lines that evidence it. Writes its analysis to disk and returns a compact record. Use for a single requirement; use... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/spec-to-code-compliance/agents/spec-compliance-checker.md." |
| `plugins/verification/spec-to-code-compliance/README.md` | Spec-to-Code Compliance: Check code against the documentation that specifies it. Every gap is either a bug or a documentation fix, and | Human documentation. Read it for install notes and extra details. |

#### writing-lean-proofs

Folder: [plugins/verification/writing-lean-proofs/](plugins/verification/writing-lean-proofs/)  |  [README](plugins/verification/writing-lean-proofs/README.md)  |  [AGENTS.md](plugins/verification/writing-lean-proofs/AGENTS.md)

Structured Lean 4 proof writing and library design following Mathlib conventions

##### Skill: writing-lean-proofs

Entry point: `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md`

Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or specifications in Lean 4, defining new types or definitions in a Lean library, reviewing Lean proofs for readability and maintainability, refactoring long tactic proofs into lemmas, filling in sorry placeholders in a Lean development, setting up CI or linters for a Lean project, diagnosing slow proofs or maxHeartbeats timeouts, or writing custom tactics, macros, or linters.

Use it when:

- Proving theorems in Lean 4, from single lemmas to multi-file developments
- Formalizing mathematics, protocols, or software specifications in Lean
- Defining new types, structures, or functions in a Lean library
- Reviewing Lean code for readability, maintainability, or Mathlib readiness
- Refactoring a long or fragile tactic proof into lemmas
- Setting up a formalization project that several people or agents will
- Setting up CI, linters, or verification gates for a Lean project - do this

Do not use it when:

- Lean 4 as a general-purpose programming language (no proofs involved) -
- Coq, Isabelle, Agda, or Lean 3 - conventions and tactic names differ;
- Verified-software Lean projects with their own house style (e.g.

Requests you can copy:

- **Use:** `Use plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md on this repository. Write the result and the evidence to ./reports/writing-lean-proofs.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md` | Writes and reviews structured Lean 4 proofs and designs Lean libraries following Mathlib conventions. Use when proving theorems in Lean, formalizing mathematics or specifications in Lean 4, defining new types or definitions in... | Start here. Say: "Follow plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md on this repository." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/anti-patterns.md` | Anti-patterns: Each entry: what it is, why it is harmful (not just that it is), and which | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/anti-patterns.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/library-design.md` | Library design: definitions, APIs, and project decomposition: How Mathlib and the large formalization projects structure theory | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/library-design.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/linting.md` | Linting: gates in CI early, custom linters for your own constructs: Set up an appropriate linter set, gated in CI, at the start of the project - and | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/linting.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/llm-techniques.md` | LLM-specific techniques: Techniques with direct evidence for model-written Lean, primarily from | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/llm-techniques.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/naming-conventions.md` | Naming conventions: Mathlib names are computable from statements. This matters doubly for LLMs: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/naming-conventions.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/performance.md` | Elaboration and reduction cost: Slow proofs and heartbeat timeouts are measurement problems before they are | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/performance.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/proof-style.md` | Tactic proof style: How to structure the inside of a proof. Sources: Mathlib style and PR review | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/proof-style.md before you start." |
| `plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/tactics.md` | Writing tactics and metaprograms: Custom tactics, macros, simprocs, and elaborators have distinctive failure modes. A bug can | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/writing-lean-proofs/skills/writing-lean-proofs/references/tactics.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/writing-lean-proofs/README.md` | writing-lean-proofs: Structured Lean 4 proof writing and library design following Mathlib | Human documentation. Read it for install notes and extra details. |

#### secret-wipe-audit

Folder: [plugins/verification/secret-wipe-audit/](plugins/verification/secret-wipe-audit/)  |  [README](plugins/verification/secret-wipe-audit/README.md)  |  [AGENTS.md](plugins/verification/secret-wipe-audit/AGENTS.md)

Detects missing or compiler-optimized zeroization of sensitive data with assembly and control-flow analysis

##### Skill: secret-wipe-audit

Entry point: `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md`

Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling secrets, keys, passwords, or other sensitive data.

Use it when:

- Auditing cryptographic implementations (keys, seeds, nonces, secrets)
- Reviewing authentication systems (passwords, tokens, session data)
- Analyzing code that handles PII or sensitive credentials
- Verifying secure cleanup in security-critical codebases
- Investigating memory safety of sensitive data handling

Do not use it when:

- General code review without security focus
- Performance optimization (unless related to secure wiping)
- Refactoring tasks not related to sensitive data
- Code without identifiable secrets or sensitive values

Requests you can copy:

- **Find:** `Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md. Scan the C/C++ or Rust code that handles secrets in ./src. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md. Scan the C/C++ or Rust code that handles secrets in ./src. Write a detailed report to ./reports/secret-wipe-audit.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/secret-wipe-audit.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md` | Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly-level analysis, and control-flow verification. Use for auditing C/C++/Rust code handling... | Start here. Say: "Follow plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/SKILL.md on the C/C++ or Rust code that handles secrets in ./src." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/prompts/report_template.md` | Zeroize Audit Report: Run ID: <run_id> | Prompt part used by the review workflow. Say: "Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/prompts/report_template.md as the prompt for that pass." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/prompts/system.md` | secret-wipe-audit (Agent Skill): Audits C/C++/Rust code for missing zeroization and compiler-removed wipes. | Prompt part used by the review workflow. Say: "Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/prompts/system.md as the prompt for that pass." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/prompts/task.md` | Task: Run secret-wipe-audit. | Prompt part used by the review workflow. Say: "Use plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/prompts/task.md as the prompt for that pass." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/compile-commands.md` | Working with compile_commands.json: This reference covers how to generate and use compile_commands.json for the secret-wipe-audit IR/ASM analysis pipeline. Read this before running Step 7 (IR comparison) or Step 8 (assembly... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/compile-commands.md before you start." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/detection-strategy.md` | Detection Strategy: Read this during execution to guide per-step analysis. Steps 1-6 are Phase 1 (source-level); Steps 7-12 are Phase 2 (compiler-level). | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/detection-strategy.md before you start." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/ir-analysis.md` | LLVM IR Analysis for Zeroization Auditing: This reference covers multi-level IR analysis for detecting compiler-optimized zeroization (dead-store elimination of wipes) and interpreting results. Read this during Step 7 (IR... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/ir-analysis.md before you start." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/mcp-analysis.md` | MCP-Assisted Semantic Analysis: This reference covers how to configure, query, and interpret Serena MCP evidence during the secret-wipe-audit semantic pass. For compile DB generation and flag extraction, refer to the... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/mcp-analysis.md before you start." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/poc-generation.md` | PoC Crafting Reference: Each secret-wipe-audit finding is demonstrated with a bespoke proof-of-concept program | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/poc-generation.md before you start." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/rust-zeroization-patterns.md` | Rust Zeroization Patterns Reference: This reference documents vulnerability pattern detected by the secret-wipe-audit tooling for Rust code. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/references/rust-zeroization-patterns.md before you start." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-0-preflight.md` | Phase 0 - Preflight, Configuration, and Work Directory: None - this is the first phase. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-0-preflight.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-1-source-analysis.md` | Phase 1 - MCP Resolution and Source Analysis: Skip if mcp_mode=off or routing.mcp_available=false or language_mode=rust (MCP is C/C++ only). | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-1-source-analysis.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-2-compiler-analysis.md` | Phase 2 - Compiler Analysis: Skip if language_mode=rust or tu-map.json has no C/C++ entries. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-2-compiler-analysis.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-3-interim-report.md` | Phase 3 - Interim Finding Collection: Spawn agent secret-wipe-audit:4-report-assembler via Task (subagent_type: "secret-wipe-audit:4-report-assembler") with: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-3-interim-report.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-4-poc-generation.md` | Phase 4 - PoC Generation: Spawn agent secret-wipe-audit:5-poc-generator via Task (subagent_type: "secret-wipe-audit:5-poc-generator") with: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-4-poc-generation.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-5-poc-validation.md` | Phase 5 - PoC Validation & Verification: Spawn agent secret-wipe-audit:5b-poc-validator via Task (subagent_type: "secret-wipe-audit:5b-poc-validator") with: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-5-poc-validation.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-6-final-report.md` | Phase 6 - Report Finalization: Spawn agent secret-wipe-audit:4-report-assembler via Task (subagent_type: "secret-wipe-audit:4-report-assembler") with: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-6-final-report.md and run that phase." |
| `plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-7-test-generation.md` | Phase 7 - Test Generation: Spawn agent secret-wipe-audit:6-test-generator via Task (subagent_type: "secret-wipe-audit:6-test-generator") with: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/secret-wipe-audit/skills/secret-wipe-audit/workflows/phase-7-test-generation.md and run that phase." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/secret-wipe-audit/agents/0-preflight.md` | Performs preflight validation, config merging, TU enumeration, and work directory setup for secret-wipe-audit. Produces merged-config.yaml, preflight.json, and orchestrator-state.json. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/0-preflight.md." |
| `plugins/verification/secret-wipe-audit/agents/1-mcp-resolver.md` | Resolves symbol definitions, types, and cross-file references using Serena MCP for secret-wipe-audit. Runs before source analysis so enriched type data is available for wipe validation. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/1-mcp-resolver.md." |
| `plugins/verification/secret-wipe-audit/agents/2-source-analyzer.md` | Identifies sensitive objects, detects wipe calls, validates correctness, and performs data-flow/heap analysis for secret-wipe-audit. Produces the sensitive object list and source-level findings consumed by compiler analysis... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/2-source-analyzer.md." |
| `plugins/verification/secret-wipe-audit/agents/2b-rust-source-analyzer.md` | Performs source-level zeroization analysis for Rust crates in secret-wipe-audit. Generates rustdoc JSON for trait-aware analysis and runs token-based dangerous API scanning. Produces sensitive objects and source findings... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/2b-rust-source-analyzer.md." |
| `plugins/verification/secret-wipe-audit/agents/3-tu-compiler-analyzer.md` | Performs per-TU compiler-level analysis (IR diff, assembly, semantic IR, CFG) for secret-wipe-audit. One instance runs per translation unit, enabling parallel execution across TUs. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/3-tu-compiler-analyzer.md." |
| `plugins/verification/secret-wipe-audit/agents/3b-rust-compiler-analyzer.md` | Performs crate-level MIR and LLVM IR analysis for Rust in secret-wipe-audit. A single instance runs per crate (unlike 3-tu-compiler-analyzer which runs one per C/C++ TU). Detects dead-store elimination of wipes, stack... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/3b-rust-compiler-analyzer.md." |
| `plugins/verification/secret-wipe-audit/agents/4-report-assembler.md` | Collects all findings from source and compiler analysis, applies supersessions and confidence gates, normalizes IDs, and produces a comprehensive markdown report with structured JSON for downstream tools. Supports dual-mode... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/4-report-assembler.md." |
| `plugins/verification/secret-wipe-audit/agents/5-poc-generator.md` | Crafts bespoke proof-of-concept programs demonstrating that secret-wipe-audit findings are exploitable. Reads source code and finding details to generate tailored PoCs - each PoC is individually written, not templated. Each... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/5-poc-generator.md." |
| `plugins/verification/secret-wipe-audit/agents/5b-poc-validator.md` | Compiles and runs all PoCs for secret-wipe-audit findings. Produces poc_validation_results.json consumed by the verification agent and the orchestrator. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/5b-poc-validator.md." |
| `plugins/verification/secret-wipe-audit/agents/5c-poc-verifier.md` | Verifies that each secret-wipe-audit PoC actually proves the vulnerability it claims to demonstrate. Reads PoC source code, finding details, and original source to check alignment between the PoC and the finding. Produces... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/5c-poc-verifier.md." |
| `plugins/verification/secret-wipe-audit/agents/6-test-generator.md` | Generates runtime validation test harnesses (C tests, MSAN, Valgrind targets) for confirmed secret-wipe-audit findings. Produces a Makefile for automated test execution. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/verification/secret-wipe-audit/agents/6-test-generator.md." |
| `plugins/verification/secret-wipe-audit/README.md` | secret-wipe-audit (Agent Skill): Audits C/C++/Rust code for missing zeroization and compiler-removed wipes. | Human documentation. Read it for install notes and extra details. |

#### mutation-testing

Folder: [plugins/verification/mutation-testing/](plugins/verification/mutation-testing/)  |  [README](plugins/verification/mutation-testing/README.md)  |  [AGENTS.md](plugins/verification/mutation-testing/AGENTS.md)

Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or finding bugs from surviving mutations.

##### Skill: mutation-testing

Entry point: `plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md`

Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or finding bugs from surviving mutations.

Use it when:

- Mentions "mutator", "mutator-sol", or "mutation testing"
- Wants to configure, scope, or speed up a mutation testing campaign
- Wants to analyze mutation results - surviving/uncaught mutants, equivalent mutants, kill rate
- Wants to use mutation results to find bugs in the source code

Requests you can copy:

- **Check:** `Use plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md. Here is the finding or change to check: <paste it or give the file path>. Tell me the verdict and show the evidence.`
- **Report:** `Use plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md on <finding, patch, or test suite>. Write a detailed report to ./reports/mutation-testing.md with the verdict and the evidence for it.`
- **Fix:** `Read ./reports/mutation-testing.md. Fix only what the report confirms. Do not touch items it rejects. Run the checks again after each fix.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md` | Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or... | Start here. Say: "Follow plugins/verification/mutation-testing/skills/mutation-testing/SKILL.md on this repository." |
| `plugins/verification/mutation-testing/skills/mutation-testing/references/blockchain-patterns.md` | Blockchain-Specific Patterns: Blockchain-specific mutation testing patterns for Solidity, FunC/Tolk, Move, and Solana Rust codebases. These patterns extend the general equivalence catalog and severity criteria; where they... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/mutation-testing/skills/mutation-testing/references/blockchain-patterns.md before you start." |
| `plugins/verification/mutation-testing/skills/mutation-testing/references/equivalent-mutants.md` | Equivalent Mutant Catalog: Equivalent mutants are mutations that produce semantically identical behavior to the original code. They are false positives in mutation testing: no test can kill them because no observable... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/mutation-testing/skills/mutation-testing/references/equivalent-mutants.md before you start." |
| `plugins/verification/mutation-testing/skills/mutation-testing/references/input-formats.md` | Input Format Examples: Parsing anchors for mutation testing tools with non-standard output formats. Most tools (mutmut, cargo-mutants, mutahunter) produce straightforward JSON or CSV that can be parsed directly from field... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/mutation-testing/skills/mutation-testing/references/input-formats.md before you start." |
| `plugins/verification/mutation-testing/skills/mutation-testing/references/optimization-strategies.md` | Optimization Strategies: Apply these strategies before running a campaign when Phase 3 of the configuration workflow requires optimization (estimated >16 hours or user requests). | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/mutation-testing/skills/mutation-testing/references/optimization-strategies.md before you start." |
| `plugins/verification/mutation-testing/skills/mutation-testing/references/report-template.md` | Mutation Testing Analysis Report: Project: [Project Name] | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/mutation-testing/skills/mutation-testing/references/report-template.md before you start." |
| `plugins/verification/mutation-testing/skills/mutation-testing/references/severity-classification.md` | Severity Classification Guide: Severity depends on the impact type of the mutated code, not the mutation operator used. The same operator replacement carries different severity depending on whether it occurs in access control... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/verification/mutation-testing/skills/mutation-testing/references/severity-classification.md before you start." |
| `plugins/verification/mutation-testing/skills/mutation-testing/workflows/analyzing-results.md` | Analyzing Mutation Testing Results: Analyzes mutation testing campaign results to identify testing gaps, classify surviving mutants by severity, filter equivalent mutants, and produce a structured report. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/mutation-testing/skills/mutation-testing/workflows/analyzing-results.md and run that phase." |
| `plugins/verification/mutation-testing/skills/mutation-testing/workflows/bug-hunter.md` | Bug Hunting with Mutation Testing: Uses mutation testing results as a map to untested code, then hunts for real bugs there. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/mutation-testing/skills/mutation-testing/workflows/bug-hunter.md and run that phase." |
| `plugins/verification/mutation-testing/skills/mutation-testing/workflows/configuration.md` | Configuration and Optimization Guide: Guide for configuring mutator and optimizing mutation testing performance before running a campaign. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/verification/mutation-testing/skills/mutation-testing/workflows/configuration.md and run that phase." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/verification/mutation-testing/README.md` | Mutation Testing: Configure mutation testing campaigns, explain what surviving mutations reveal about tests, and investigate potential bugs in the affected code. | Human documentation. Read it for install notes and extra details. |

### Reverse Engineering

#### dwarf-debug-info

Folder: [plugins/reverse-engineering/dwarf-debug-info/](plugins/reverse-engineering/dwarf-debug-info/)  |  [README](plugins/reverse-engineering/dwarf-debug-info/README.md)  |  [AGENTS.md](plugins/reverse-engineering/dwarf-debug-info/AGENTS.md)

Analyze DWARF debug information: parse and search DIEs with dwarfdump and readelf, verify debug info integrity, and write DWARF parsing code

##### Skill: dwarf-debug-info

Entry point: `plugins/reverse-engineering/dwarf-debug-info/skills/dwarf-debug-info/SKILL.md`

Analyzes DWARF debug information in compiled binaries. Use when inspecting .debug_* sections, DIE trees, or DW_TAG_/DW_AT_ entries with dwarfdump/llvm-dwarfdump or readelf, verifying debug info with llvm-dwarfdump --verify, answering DWARF standard questions, or writing code that parses DWARF (libdwarf, pyelftools, gimli).

Requests you can copy:

- **Use:** `Use plugins/reverse-engineering/dwarf-debug-info/skills/dwarf-debug-info/SKILL.md. Task: <describe what you want>. Target: this repository.`
- **Save the output:** `Use plugins/reverse-engineering/dwarf-debug-info/skills/dwarf-debug-info/SKILL.md on this repository. Write the result and the evidence to ./reports/dwarf-debug-info.md.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/reverse-engineering/dwarf-debug-info/skills/dwarf-debug-info/SKILL.md` | Analyzes DWARF debug information in compiled binaries. Use when inspecting .debug_* sections, DIE trees, or DW_TAG_/DW_AT_ entries with dwarfdump/llvm-dwarfdump or readelf, verifying debug info with llvm-dwarfdump --verify,... | Start here. Say: "Follow plugins/reverse-engineering/dwarf-debug-info/skills/dwarf-debug-info/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/reverse-engineering/dwarf-debug-info/README.md` | DWARF Expert: Interact with and analyze DWARF debug information: parse and search DIEs with | Human documentation. Read it for install notes and extra details. |

### Mobile Security

#### firebase-apk-scanner

Folder: [plugins/mobile-security/firebase-apk-scanner/](plugins/mobile-security/firebase-apk-scanner/)  |  [README](plugins/mobile-security/firebase-apk-scanner/README.md)  |  [AGENTS.md](plugins/mobile-security/firebase-apk-scanner/AGENTS.md)

Scan Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. For authorized security research only.

##### Skill: firebase-apk-scanner

Entry point: `plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md`

Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing mobile app security audits, or testing Firebase endpoint security. For authorized security research only.

Use it when:

- Auditing Android applications for Firebase security misconfigurations
- Testing Firebase endpoints extracted from APKs (Realtime Database, Firestore, Storage)
- Checking authentication security (open signup, anonymous auth, email enumeration)
- Enumerating Cloud Functions and testing for unauthenticated access
- Mobile app security assessments involving Firebase backends
- Authorized penetration testing of Firebase-backed applications

Do not use it when:

- Scanning apps you do not have explicit authorization to test
- Testing production Firebase projects without written permission
- When you only need to extract Firebase config without testing (use manual grep/strings instead)
- For non-Android targets (iOS, web apps) - this skill is APK-specific
- When the target app does not use Firebase

Requests you can copy:

- **Find:** `Use plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md. Scan the Android app at ./app.apk. List every vulnerability you find, with file, line, and why it is a problem. Do not change any code.`
- **Report:** `Use plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md. Scan the Android app at ./app.apk. Write a detailed report to ./reports/firebase-apk-scanner.md. For each issue give severity, evidence, steps to reproduce, and a suggested fix. Do not change any code yet.`
- **Fix:** `Read ./reports/firebase-apk-scanner.md. Fix the issues one at a time, highest severity first. After each fix, check it again and note the result in the report.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md` | Scans Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. Use when analyzing APK files for Firebase vulnerabilities, performing... | Start here. Say: "Follow plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md on the Android app at ./app.apk." |
| `plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/references/vulnerabilities.md` | Firebase Security Vulnerability Patterns: Detailed vulnerability patterns, exploitation techniques, and audit checklists for Firebase implementations in mobile applications. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/mobile-security/firebase-apk-scanner/skills/firebase-apk-scanner/references/vulnerabilities.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/mobile-security/firebase-apk-scanner/commands/scan-apk.md` | Scans Android APKs for Firebase security misconfigurations | Saved prompt. Say: "Follow plugins/mobile-security/firebase-apk-scanner/commands/scan-apk.md on the Android app at ./app.apk." |
| `plugins/mobile-security/firebase-apk-scanner/README.md` | Firebase APK Security Scanner: Scan Android APKs for Firebase security misconfigurations including open databases, exposed storage buckets, and authentication bypasses. | Human documentation. Read it for install notes and extra details. |

### Development

#### code-improver

Folder: [plugins/development/code-improver/](plugins/development/code-improver/)  |  [README](plugins/development/code-improver/README.md)  |  [AGENTS.md](plugins/development/code-improver/AGENTS.md)

Improves code targets - skills, plugins, or a branch's changes - through an autonomous review-and-fix workflow with a pluggable reviewer (any installed skill or agent), a cross-round findings ledger, oscillation escalation, and a mechanical scope guard.

##### Skill: code-improver

Entry point: `plugins/development/code-improver/skills/code-improver/SKILL.md`

Runs an autonomous review-and-fix improvement loop over any code target - a skill, plugin, module, or directory - using a reviewer the user names: any installed skill or agent. Keeps a cross-round findings ledger, escalates when fixes stop converging, and guards scope mechanically. Use when asked to 'improve this code until review passes', 'run an improvement loop with <reviewer>', or to iterate review-and-fix with a specific reviewer. For skills prefer the skill-improver entry; for a branch prefer pr-improver.

Do not use it when:

- **A Claude Code skill**: use the `skill-improver` entry - it wires the right reviewer
- **A branch / pull request**: use the `pr-improver` entry - it derives scope from the diff
- **One-time review**: dispatch the reviewer directly; the loop's value is iteration
- **Quick single fixes**: edit the file directly

Requests you can copy:

- **Use:** `Use plugins/development/code-improver/skills/code-improver/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/code-improver/skills/code-improver/SKILL.md` | Runs an autonomous review-and-fix improvement loop over any code target - a skill, plugin, module, or directory - using a reviewer the user names: any installed skill or agent. Keeps a cross-round findings ledger, escalates... | Start here. Say: "Follow plugins/development/code-improver/skills/code-improver/SKILL.md on this repository." |

##### Skill: pr-improver

Entry point: `plugins/development/code-improver/skills/pr-improver/SKILL.md`

Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the branch touched. Reviews are performed by an installed PR-review skill (default: pr-review-toolkit's review-pr). Use to fix review findings on a branch before opening or updating a pull request ('clean up this branch', 'fix this PR until review passes', 'run review-and-fix on my changes'). NOT for a one-time review - run the PR-review skill directly.

Do not use it when:

- **One-time review**: run the PR-review skill directly; the loop's value is iteration
- **A skill**: use the `skill-improver` entry - it wires the right reviewer
- **Unpushed exploratory work**: review-and-fix loops harden a diff; while the shape is

Requests you can copy:

- **Use:** `Use plugins/development/code-improver/skills/pr-improver/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/code-improver/skills/pr-improver/SKILL.md` | Runs an autonomous review-and-fix improvement loop over the current branch's changes until a PR review comes back clean, scoped mechanically to the directories the branch touched. Reviews are performed by an installed... | Start here. Say: "Follow plugins/development/code-improver/skills/pr-improver/SKILL.md on this repository." |

##### Skill: skill-improver

Entry point: `plugins/development/code-improver/skills/skill-improver/SKILL.md`

Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes stop converging, and a mechanical scope guard. Reviews are performed by the plugin-dev skill-reviewer agent. Use to fix skill quality issues, iteratively refine a skill, or resume a loop after an escalation ('fix my skill', 'improve this skill until it passes review', 'skill improvement loop'). NOT for a one-time review - use the plugin-dev skill-reviewer agent directly.

Do not use it when:

- **One-time review**: dispatch the `plugin-dev:skill-reviewer` agent directly
- **Quick single fixes**: edit the file directly
- **Non-skill targets**: use the `code-improver` skill with a reviewer that fits the
- **Exploratory drafting**: manual iteration gives more control while the shape is fluid

Requests you can copy:

- **Use:** `Use plugins/development/code-improver/skills/skill-improver/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/code-improver/skills/skill-improver/SKILL.md` | Runs an autonomous review-and-fix improvement loop over a Claude Code skill until a review comes back clean, with a cross-round findings ledger, escalation when fixes stop converging, and a mechanical scope guard. Reviews are... | Start here. Say: "Follow plugins/development/code-improver/skills/skill-improver/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/code-improver/agents/fixer.md` | Applies fixes for the blocking findings dispatched by the /code-improver:improve workflow and returns one verdict per finding (fixed, rejected, or deferred) under a hard scope and git-safety contract. Dispatched by the... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/development/code-improver/agents/fixer.md." |
| `plugins/development/code-improver/README.md` | Code Improver Plugin: Improves a code target through an autonomous review→fix loop. | Human documentation. Read it for install notes and extra details. |

#### devcontainer-setup

Folder: [plugins/development/devcontainer-setup/](plugins/development/devcontainer-setup/)  |  [README](plugins/development/devcontainer-setup/README.md)  |  [AGENTS.md](plugins/development/devcontainer-setup/AGENTS.md)

Create pre-configured devcontainers with Claude Code and language-specific tooling

##### Skill: devcontainer-setup

Entry point: `plugins/development/devcontainer-setup/skills/devcontainer-setup/SKILL.md`

Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring sandboxed Claude Code workspaces.

Use it when:

- User asks to "set up a devcontainer" or "add devcontainer support"
- User wants a sandboxed Claude Code development environment
- User needs isolated development environments with persistent configuration

Do not use it when:

- User already has a devcontainer configuration and just needs modifications
- User is asking about general Docker or container questions
- User wants to deploy production containers (this is for development only)

Requests you can copy:

- **Use:** `Use plugins/development/devcontainer-setup/skills/devcontainer-setup/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/devcontainer-setup/skills/devcontainer-setup/SKILL.md` | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devcontainer support to a project, setting up isolated development environments, or configuring... | Start here. Say: "Follow plugins/development/devcontainer-setup/skills/devcontainer-setup/SKILL.md on this repository." |
| `plugins/development/devcontainer-setup/skills/devcontainer-setup/references/dockerfile-best-practices.md` | Dockerfile Best Practices: Choose minimal, trusted base images: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/devcontainer-setup/skills/devcontainer-setup/references/dockerfile-best-practices.md before you start." |
| `plugins/development/devcontainer-setup/skills/devcontainer-setup/references/features-vs-dockerfile.md` | Features vs Dockerfile: For Python, we use Dockerfile + uv instead of the Python feature because: | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/devcontainer-setup/skills/devcontainer-setup/references/features-vs-dockerfile.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/devcontainer-setup/README.md` | Devcontainer Setup Plugin: Create pre-configured devcontainers with Claude Code and language-specific tooling. | Human documentation. Read it for install notes and extra details. |

#### gh-cli

Folder: [plugins/development/gh-cli/](plugins/development/gh-cli/)  |  [README](plugins/development/gh-cli/README.md)  |  [AGENTS.md](plugins/development/gh-cli/AGENTS.md)

Intercepts GitHub URL fetches (WebFetch and MCP fetch tools) and curl/wget commands, redirecting to the authenticated gh CLI.

##### Skill: gh-cli

Entry point: `plugins/development/gh-cli/skills/gh-cli/SKILL.md`

Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues.

Use it when:

- Working with GitHub repositories, pull requests, issues, releases, or raw file URLs.
- You need authenticated access to private repositories or higher API rate limits.
- You are about to use `curl`, `wget`, `WebFetch`, or an MCP fetch tool against GitHub.

Do not use it when:

- The target is not GitHub.
- Plain local git operations already solve the task.

Requests you can copy:

- **Use:** `Use plugins/development/gh-cli/skills/gh-cli/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/gh-cli/skills/gh-cli/SKILL.md` | Enforces authenticated gh CLI workflows over unauthenticated curl, WebFetch, and MCP fetch patterns. Use when working with GitHub URLs, API access, pull requests, or issues. | Start here. Say: "Follow plugins/development/gh-cli/skills/gh-cli/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/gh-cli/README.md` | gh-cli: A Claude Code plugin that intercepts GitHub URL fetches and redirects Claude to use the authenticated gh CLI instead. | Human documentation. Read it for install notes and extra details. |

#### git-cleanup

Folder: [plugins/development/git-cleanup/](plugins/development/git-cleanup/)  |  [README](plugins/development/git-cleanup/README.md)  |  [AGENTS.md](plugins/development/git-cleanup/AGENTS.md)

Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work.

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/git-cleanup/commands/git-cleanup.md` | Safely analyzes and cleans up local git branches and worktrees, categorizing them as merged, squash-merged, superseded, or active work before deleting anything. | Saved prompt. Say: "Follow plugins/development/git-cleanup/commands/git-cleanup.md on this repository." |
| `plugins/development/git-cleanup/README.md` | git-cleanup: An agent command for safely cleaning up accumulated git worktrees and local branches. | Human documentation. Read it for install notes and extra details. |
| `plugins/development/git-cleanup/references/merge-evidence.md` | Merge Evidence Standard: What counts as proof that a branch's work is already in the default branch, and what does not. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/git-cleanup/references/merge-evidence.md before you start." |

#### github-triage

Folder: [plugins/development/github-triage/](plugins/development/github-triage/)  |  [README](plugins/development/github-triage/README.md)  |  [AGENTS.md](plugins/development/github-triage/AGENTS.md)

Triages a repository's open GitHub issues and pull requests via the gh CLI: optionally merges ready bot and maintainer-approved PRs and spawns review subagents for unreviewed ones, closes already-resolved issues with referenced explanations, cross-links issues with pending fix PRs, and assigns local-only priority and change-size estimates.

##### Skill: github-triage

Entry point: `plugins/development/github-triage/skills/github-triage/SKILL.md`

Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs - incrementally merging passing automated/bot PRs and maintainer-approved ones, and spawning review subagents for never-reviewed ones - then closes already-resolved issues with comments citing the resolving PR or commit, cross-links issues with their pending fix PRs, and assigns local-only priority and change-size estimates for everything outstanding. Use when triaging, grooming, or reviewing a repository's open issues and PRs.

Use it when:

- When the user runs `/github-triage` to groom or review a repository's open issues
- When an issue backlog has drifted: resolved work left open, fixes landed without
- When ready PRs have piled up (passing dependency bumps, approved-and-green PRs) or

Do not use it when:

- Do not invoke automatically. This skill performs irreversible GitHub writes
- Do not use to apply priority/effort *labels* on GitHub. Priority and size are
- Do not use as a substitute for a human's final merge decision - every merge is

Requests you can copy:

- **Use:** `Use plugins/development/github-triage/skills/github-triage/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/github-triage/skills/github-triage/SKILL.md` | Triages a repository's open GitHub issues and pull requests via the gh CLI. Optionally reviews and merges ready PRs - incrementally merging passing automated/bot PRs and maintainer-approved ones, and spawning review subagents... | Start here. Say: "Follow plugins/development/github-triage/skills/github-triage/SKILL.md on this repository." |
| `plugins/development/github-triage/skills/github-triage/references/reviewing-prs.md` | Reviewing open pull requests: Rubric for the PR-review subagents the github-triage skill spawns in Phase 2 for | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/github-triage/skills/github-triage/references/reviewing-prs.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/github-triage/README.md` | github-triage: A Claude Code skill for triaging the open GitHub issues and pull requests of a | Human documentation. Read it for install notes and extra details. |

#### goal-prompt

Folder: [plugins/development/goal-prompt/](plugins/development/goal-prompt/)  |  [README](plugins/development/goal-prompt/README.md)  |  [AGENTS.md](plugins/development/goal-prompt/AGENTS.md)

Drafts copy-ready /goal commands for goal mode in Claude Code and Codex: verifiable completion conditions with stop bounds, normalized to a single line under the 4,000-character cap.

##### Skill: goal-prompt

Entry point: `plugins/development/goal-prompt/skills/goal-prompt/SKILL.md`

Drafts copy-paste-ready /goal commands for goal mode in Claude Code and Codex. Use when the user asks to create, write, rewrite, improve, compress, clean up, or prepare a goal prompt, goal condition, /goal command, goal-mode objective, or copy-ready long-running task objective.

Requests you can copy:

- **Use:** `Use plugins/development/goal-prompt/skills/goal-prompt/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/goal-prompt/skills/goal-prompt/SKILL.md` | Drafts copy-paste-ready /goal commands for goal mode in Claude Code and Codex. Use when the user asks to create, write, rewrite, improve, compress, clean up, or prepare a goal prompt, goal condition, /goal command, goal-mode... | Start here. Say: "Follow plugins/development/goal-prompt/skills/goal-prompt/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/goal-prompt/README.md` | goal-prompt: Turns a task description into a copy-paste-ready /goal command for goal mode in Claude Code or Codex. | Human documentation. Read it for install notes and extra details. |

#### random-pick

Folder: [plugins/development/random-pick/](plugins/development/random-pick/)  |  [README](plugins/development/random-pick/README.md)  |  [AGENTS.md](plugins/development/random-pick/AGENTS.md)

Draws the 12 Houses of the Zodiac Tarot spread using cryptographic randomness to add 100+ bits of entropy to vague or underspecified planning. Interprets the spread to guide next steps. Use when feeling lucky, invoking heart-of-the-cards energy, or when prompts are ambiguous.

##### Skill: random-pick

Entry point: `plugins/development/random-pick/skills/random-pick/SKILL.md`

Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide', 'YOLO', 'whatever', 'idk', or other nonchalant phrases, makes Yu-Gi-Oh references, or when you are about to arbitrarily pick between multiple reasonable approaches. Prefer over asking clarifying questions when the user's tone is casual or playful rather than precision-seeking.

Use it when:

- **Vague prompts**: The user's request is ambiguous and multiple reasonable approaches exist
- **Explicit invocations**: "I'm feeling lucky", "let fate decide", "dealer's choice", "surprise me", "whatever you think", "YOLO"
- **Casual delegation**: "whatever", "up to you", "your call", "idk", "just do something", "wing it", "I trust you", "doesn't matter", "do what you want", "I don't care", "any approach works", "you pick"
- **Yu-Gi-Oh energy**: "Heart of the cards", "I believe in the heart of the cards", "you've activated my trap card", "it's time to duel"
- **Shrug-like brevity**: Very short prompts that fully delegate the decision without expressing a preference
- **Redraw requests**: "Try again" or "draw again" when no actual system changes occurred (this means draw new cards, not re-run the same approach)
- **Tie-breaking**: When you are about to arbitrarily pick between 2+ valid approaches, draw cards instead of silently choosing one

Do not use it when:

- The user has given clear, specific instructions
- The task has a single obvious correct approach
- As the deciding authority for safety-critical work (security, data integrity,
- The user explicitly asks you NOT to use Tarot
- The user's tone is precision-seeking rather than casual -- ask clarifying questions instead to gather actual requirements

Requests you can copy:

- **Use:** `Use plugins/development/random-pick/skills/random-pick/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/random-pick/skills/random-pick/SKILL.md` | Draws the 12 Houses of the Zodiac Tarot spread to inject entropy into planning when prompts are vague, ambiguous, or casually delegated. Interprets the spread to guide next steps. Use when the user says 'let fate decide',... | Start here. Say: "Follow plugins/development/random-pick/skills/random-pick/SKILL.md on this repository." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/ace-of-cups.md` | Ace of Cups: Suit: Cups / Rank: Ace | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/ace-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/eight-of-cups.md` | Eight of Cups: Suit: Cups / Rank: 8 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/eight-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/five-of-cups.md` | Five of Cups: Suit: Cups / Rank: 5 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/five-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/four-of-cups.md` | Four of Cups: Suit: Cups / Rank: 4 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/four-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/king-of-cups.md` | King of Cups: Suit: Cups / Rank: King | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/king-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/knight-of-cups.md` | Knight of Cups: Suit: Cups / Rank: Knight | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/knight-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/nine-of-cups.md` | Nine of Cups: Suit: Cups / Rank: 9 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/nine-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/page-of-cups.md` | Page of Cups: Suit: Cups / Rank: Page | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/page-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/queen-of-cups.md` | Queen of Cups: Suit: Cups / Rank: Queen | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/queen-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/seven-of-cups.md` | Seven of Cups: Suit: Cups / Rank: 7 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/seven-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/six-of-cups.md` | Six of Cups: Suit: Cups / Rank: 6 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/six-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/ten-of-cups.md` | Ten of Cups: Suit: Cups / Rank: 10 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/ten-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/three-of-cups.md` | Three of Cups: Suit: Cups / Rank: 3 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/three-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/cups/two-of-cups.md` | Two of Cups: Suit: Cups / Rank: 2 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/cups/two-of-cups.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/00-the-fool.md` | The Fool: Arcana: Major / Number: 0 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/00-the-fool.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/01-the-magician.md` | The Magician: Arcana: Major / Number: I | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/01-the-magician.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/02-the-high-priestess.md` | The High Priestess: Arcana: Major / Number: II | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/02-the-high-priestess.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/03-the-empress.md` | The Empress: Arcana: Major / Number: III | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/03-the-empress.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/04-the-emperor.md` | The Emperor: Arcana: Major / Number: IV | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/04-the-emperor.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/05-the-hierophant.md` | The Hierophant: Arcana: Major / Number: V | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/05-the-hierophant.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/06-the-lovers.md` | The Lovers: Arcana: Major / Number: VI | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/06-the-lovers.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/07-the-chariot.md` | The Chariot: Arcana: Major / Number: VII | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/07-the-chariot.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/08-strength.md` | Strength: Arcana: Major / Number: VIII | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/08-strength.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/09-the-hermit.md` | The Hermit: Arcana: Major / Number: IX | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/09-the-hermit.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/10-wheel-of-fortune.md` | Wheel of Fortune: Arcana: Major / Number: X | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/10-wheel-of-fortune.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/11-justice.md` | Justice: Arcana: Major / Number: XI | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/11-justice.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/12-the-hanged-man.md` | The Hanged Man: Arcana: Major / Number: XII | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/12-the-hanged-man.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/13-death.md` | Death: Arcana: Major / Number: XIII | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/13-death.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/14-temperance.md` | Temperance: Arcana: Major / Number: XIV | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/14-temperance.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/15-the-devil.md` | The Devil: Arcana: Major / Number: XV | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/15-the-devil.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/16-the-tower.md` | The Tower: Arcana: Major / Number: XVI | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/16-the-tower.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/17-the-star.md` | The Star: Arcana: Major / Number: XVII | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/17-the-star.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/18-the-moon.md` | The Moon: Arcana: Major / Number: XVIII | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/18-the-moon.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/19-the-sun.md` | The Sun: Arcana: Major / Number: XIX | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/19-the-sun.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/20-judgement.md` | Judgement: Arcana: Major / Number: XX | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/20-judgement.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/major/21-the-world.md` | The World: Arcana: Major / Number: XXI | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/major/21-the-world.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/ace-of-pentacles.md` | Ace of Pentacles: Suit: Pentacles / Rank: Ace | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/ace-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/eight-of-pentacles.md` | Eight of Pentacles: Suit: Pentacles / Rank: 8 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/eight-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/five-of-pentacles.md` | Five of Pentacles: Suit: Pentacles / Rank: 5 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/five-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/four-of-pentacles.md` | Four of Pentacles: Suit: Pentacles / Rank: 4 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/four-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/king-of-pentacles.md` | King of Pentacles: Suit: Pentacles / Rank: King | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/king-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/knight-of-pentacles.md` | Knight of Pentacles: Suit: Pentacles / Rank: Knight | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/knight-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/nine-of-pentacles.md` | Nine of Pentacles: Suit: Pentacles / Rank: 9 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/nine-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/page-of-pentacles.md` | Page of Pentacles: Suit: Pentacles / Rank: Page | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/page-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/queen-of-pentacles.md` | Queen of Pentacles: Suit: Pentacles / Rank: Queen | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/queen-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/seven-of-pentacles.md` | Seven of Pentacles: Suit: Pentacles / Rank: 7 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/seven-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/six-of-pentacles.md` | Six of Pentacles: Suit: Pentacles / Rank: 6 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/six-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/ten-of-pentacles.md` | Ten of Pentacles: Suit: Pentacles / Rank: 10 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/ten-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/three-of-pentacles.md` | Three of Pentacles: Suit: Pentacles / Rank: 3 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/three-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/pentacles/two-of-pentacles.md` | Two of Pentacles: Suit: Pentacles / Rank: 2 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/pentacles/two-of-pentacles.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/ace-of-swords.md` | Ace of Swords: Suit: Swords / Rank: Ace | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/ace-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/eight-of-swords.md` | Eight of Swords: Suit: Swords / Rank: 8 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/eight-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/five-of-swords.md` | Five of Swords: Suit: Swords / Rank: 5 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/five-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/four-of-swords.md` | Four of Swords: Suit: Swords / Rank: 4 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/four-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/king-of-swords.md` | King of Swords: Suit: Swords / Rank: King | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/king-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/knight-of-swords.md` | Knight of Swords: Suit: Swords / Rank: Knight | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/knight-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/nine-of-swords.md` | Nine of Swords: Suit: Swords / Rank: 9 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/nine-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/page-of-swords.md` | Page of Swords: Suit: Swords / Rank: Page | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/page-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/queen-of-swords.md` | Queen of Swords: Suit: Swords / Rank: Queen | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/queen-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/seven-of-swords.md` | Seven of Swords: Suit: Swords / Rank: 7 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/seven-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/six-of-swords.md` | Six of Swords: Suit: Swords / Rank: 6 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/six-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/ten-of-swords.md` | Ten of Swords: Suit: Swords / Rank: 10 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/ten-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/three-of-swords.md` | Three of Swords: Suit: Swords / Rank: 3 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/three-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/swords/two-of-swords.md` | Two of Swords: Suit: Swords / Rank: 2 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/swords/two-of-swords.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/ace-of-wands.md` | Ace of Wands: Suit: Wands / Rank: Ace | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/ace-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/eight-of-wands.md` | Eight of Wands: Suit: Wands / Rank: 8 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/eight-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/five-of-wands.md` | Five of Wands: Suit: Wands / Rank: 5 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/five-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/four-of-wands.md` | Four of Wands: Suit: Wands / Rank: 4 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/four-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/king-of-wands.md` | King of Wands: Suit: Wands / Rank: King | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/king-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/knight-of-wands.md` | Knight of Wands: Suit: Wands / Rank: Knight | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/knight-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/nine-of-wands.md` | Nine of Wands: Suit: Wands / Rank: 9 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/nine-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/page-of-wands.md` | Page of Wands: Suit: Wands / Rank: Page | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/page-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/queen-of-wands.md` | Queen of Wands: Suit: Wands / Rank: Queen | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/queen-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/seven-of-wands.md` | Seven of Wands: Suit: Wands / Rank: 7 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/seven-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/six-of-wands.md` | Six of Wands: Suit: Wands / Rank: 6 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/six-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/ten-of-wands.md` | Ten of Wands: Suit: Wands / Rank: 10 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/ten-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/three-of-wands.md` | Three of Wands: Suit: Wands / Rank: 3 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/three-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/cards/wands/two-of-wands.md` | Two of Wands: Suit: Wands / Rank: 2 | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/cards/wands/two-of-wands.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/01-first-house.md` | First House: Domain: Self, identity, agency, and first motion | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/01-first-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/02-second-house.md` | Second House: Domain: Resources, values, constraints, and preservation | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/02-second-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/03-third-house.md` | Third House: Domain: Communication, learning, interfaces, and local connections | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/03-third-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/04-fourth-house.md` | Fourth House: Domain: Foundations, history, context, and hidden dependencies | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/04-fourth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/05-fifth-house.md` | Fifth House: Domain: Creativity, experimentation, expressiveness, and delight | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/05-fifth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/06-sixth-house.md` | Sixth House: Domain: Practice, service, quality, routine, and maintenance | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/06-sixth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/07-seventh-house.md` | Seventh House: Domain: Partnership, contracts, users, and external counterparts | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/07-seventh-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/08-eighth-house.md` | Eighth House: Domain: Transformation, risk, shared state, secrets, and deep change | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/08-eighth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/09-ninth-house.md` | Ninth House: Domain: Exploration, principles, standards, and broader strategy | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/09-ninth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/10-tenth-house.md` | Tenth House: Domain: Delivery, reputation, public outcome, and long-term direction | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/10-tenth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/11-eleventh-house.md` | Eleventh House: Domain: Community, networks, systems, and shared aspirations | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/11-eleventh-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/houses/12-twelfth-house.md` | Twelfth House: Domain: Blind spots, hidden costs, endings, and unconscious assumptions | Guide loaded during the work. Say: "Read plugins/development/random-pick/skills/random-pick/houses/12-twelfth-house.md before you start." |
| `plugins/development/random-pick/skills/random-pick/references/INTERPRETATION_GUIDE.md` | Interpretation Guide: How to read the 12 Houses of the Zodiac Tarot spread and map it to technical | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/random-pick/skills/random-pick/references/INTERPRETATION_GUIDE.md before you start." |
| `plugins/development/random-pick/skills/random-pick/references/TECHNICAL_CONTEXT_LENSES.md` | Technical Context Lenses: These lenses apply across a wide range of technical workflows, but they cluster | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/random-pick/skills/random-pick/references/TECHNICAL_CONTEXT_LENSES.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/random-pick/agents/draw.md` | Draw the 12 Houses of the Zodiac Tarot spread and return a concise structured reading. Use as a named agent instead of wrapping Skill(random-pick) in an Agent call. Callers get just the verdict text; card file content stays in... | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/development/random-pick/agents/draw.md." |
| `plugins/development/random-pick/README.md` | random-pick: A Claude Code skill that draws Tarot cards using secrets to inject | Human documentation. Read it for install notes and extra details. |

#### modern-cpp

Folder: [plugins/development/modern-cpp/](plugins/development/modern-cpp/)  |  [README](plugins/development/modern-cpp/README.md)  |  [AGENTS.md](plugins/development/modern-cpp/AGENTS.md)

Modern C++ best practices (C++20/23/26). Use when writing C++ code, creating new C++ projects, or modernizing legacy C++ patterns.

##### Skill: modern-cpp

Entry point: `plugins/development/modern-cpp/skills/modern-cpp/SKILL.md`

Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces raw pointers with smart pointers, SFINAE with concepts, printf with std::print, error codes with std::expected.

Use it when:

- Writing new C++ functions, classes, or libraries
- Modernizing existing C++ code (pre-C++20 patterns)
- Choosing between legacy and modern approaches
- Working on security-critical or safety-sensitive C++
- Reviewing C++ code for modern idiom adoption

Do not use it when:

- **User explicitly requires older standard**: Respect constraints (embedded, legacy ABI)
- **Pure C code**: This skill is C++-specific
- **Build system questions**: CMake, Meson, Bazel configuration is out of scope
- **Non-C++ projects**: Mixed codebases where C++ isn't primary

Requests you can copy:

- **Use:** `Use plugins/development/modern-cpp/skills/modern-cpp/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/modern-cpp/skills/modern-cpp/SKILL.md` | Guides C++ code toward modern idioms (C++20/23/26). Use when writing new C++ code, modernizing legacy patterns, or working on security-critical C++. Replaces raw pointers with smart pointers, SFINAE with concepts, printf with... | Start here. Say: "Follow plugins/development/modern-cpp/skills/modern-cpp/SKILL.md on this repository." |
| `plugins/development/modern-cpp/skills/modern-cpp/references/anti-patterns.md` | Anti-Patterns: Legacy to Modern C++: Comprehensive reference of legacy C++ patterns and their modern replacements. Each entry explains WHY the modern version is better - not just that it exists. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-cpp/skills/modern-cpp/references/anti-patterns.md before you start." |
| `plugins/development/modern-cpp/skills/modern-cpp/references/compiler-hardening.md` | Compiler Hardening: Security-focused compiler and linker configuration for C++ projects. Based on the [OpenSSF Compiler Options Hardening... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-cpp/skills/modern-cpp/references/compiler-hardening.md before you start." |
| `plugins/development/modern-cpp/skills/modern-cpp/references/cpp20-features.md` | C++20 Features (Default Practice): These features are mature, well-supported (GCC 12+, Clang 14+, MSVC 17.0+), and should be the default way to write C++. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-cpp/skills/modern-cpp/references/cpp20-features.md before you start." |
| `plugins/development/modern-cpp/skills/modern-cpp/references/cpp23-features.md` | C++23 Features (Usable Today): These features have solid compiler support (GCC 13+, Clang 17+, MSVC 17.4+) and deliver immediate value. Adopt them now. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-cpp/skills/modern-cpp/references/cpp23-features.md before you start." |
| `plugins/development/modern-cpp/skills/modern-cpp/references/cpp26-features.md` | C++26 Features: C++26 was finalized in March 2026 - the most significant release since C++11. This reference covers the features worth knowing about, ranked by practical impact. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-cpp/skills/modern-cpp/references/cpp26-features.md before you start." |
| `plugins/development/modern-cpp/skills/modern-cpp/references/safe-idioms.md` | Safe C++ Idioms: Security patterns organized by vulnerability class. Each section explains what exploitable bugs the pattern prevents and what modern C++ features eliminate them. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-cpp/skills/modern-cpp/references/safe-idioms.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/modern-cpp/README.md` | modern-cpp: Modern C++ best practices plugin for coding agents, guiding AI-assisted development toward C++20/23/26 idioms with a security emphasis from Aevrin Security. | Human documentation. Read it for install notes and extra details. |

#### modern-python

Folder: [plugins/development/modern-python/](plugins/development/modern-python/)  |  [README](plugins/development/modern-python/README.md)  |  [AGENTS.md](plugins/development/modern-python/AGENTS.md)

Modern Python best practices. Use when creating new Python projects, and writing Python scripts, or migrating existing projects from legacy tools.

##### Skill: modern-python

Entry point: `plugins/development/modern-python/skills/modern-python/SKILL.md`

Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black.

Use it when:

- Creating a new Python project or package
- Setting up `pyproject.toml` configuration
- Configuring development tools (linting, formatting, testing)
- Writing Python scripts with external dependencies
- Migrating from legacy tools (when user requests it)

Do not use it when:

- **User wants to keep legacy tooling**: Respect existing workflows if explicitly requested
- **Python < 3.11 required**: These tools target modern Python
- **Non-Python projects**: Mixed codebases where Python isn't primary

Requests you can copy:

- **Use:** `Use plugins/development/modern-python/skills/modern-python/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/modern-python/skills/modern-python/SKILL.md` | Configures Python projects with modern tooling (uv, ruff, ty). Use when creating projects, writing standalone scripts, or migrating from pip/Poetry/mypy/black. | Start here. Say: "Follow plugins/development/modern-python/skills/modern-python/SKILL.md on this repository." |
| `plugins/development/modern-python/skills/modern-python/references/dependabot.md` | Dependabot: Automated Dependency Updates: [Dependabot](https://docs.github.com/en/code-security/dependabot) automatically creates pull requests to keep your dependencies up to date. GitHub hosts it natively-no external service... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/dependabot.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/migration-checklist.md` | Migration Checklist: Comprehensive checklist for migrating Python projects to modern tooling. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/migration-checklist.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/pep723-scripts.md` | PEP 723: Inline Script Metadata: PEP 723 allows embedding dependency metadata directly in Python scripts, eliminating the need for separate requirements.txt or pyproject.toml files for simple scripts. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/pep723-scripts.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/prek.md` | prek: Fast Pre-commit Hooks: [prek](https://github.com/j178/prek) is a fast, Rust-native drop-in replacement for pre-commit. It uses the same .pre-commit-config.yaml format and is fully compatible with existing configurations. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/prek.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/pyproject.md` | pyproject.toml Configuration Reference: Complete reference for configuring pyproject.toml for modern Python projects. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/pyproject.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/ruff-config.md` | Ruff Configuration Reference: Ruff is an extremely fast Python linter and formatter written in Rust. It replaces flake8, black, isort, pyupgrade, pydocstyle, and many other tools. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/ruff-config.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/security-setup.md` | Security Setup: Security tooling for Python projects: pre-commit hooks, CI auditing, and dependency scanning. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/security-setup.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/testing.md` | Testing with pytest: Configuration and best practices for pytest with coverage enforcement. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/testing.md before you start." |
| `plugins/development/modern-python/skills/modern-python/references/uv-commands.md` | uv Command Reference: uv is an extremely fast Python package and project manager written in Rust. It replaces pip, virtualenv, pip-tools, pipx, and pyenv. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/modern-python/skills/modern-python/references/uv-commands.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/modern-python/README.md` | Modern Python: Modern Python tooling and best practices using uv, ruff, ty, and pytest. | Human documentation. Read it for install notes and extra details. |

#### open-sourcing

Folder: [plugins/development/open-sourcing/](plugins/development/open-sourcing/)  |  [README](plugins/development/open-sourcing/README.md)  |  [AGENTS.md](plugins/development/open-sourcing/AGENTS.md)

Prepares a repository for public open-source release: secrets-history hygiene, license selection, documentation and CI readiness checks, and language-specific packaging and release guidance.

##### Skill: open-sourcing

Entry point: `plugins/development/open-sourcing/skills/open-sourcing/SKILL.md`

This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source readiness", "choose a license for this project", or "set up release automation" ahead of a public launch. Provides a release-readiness workflow covering secrets hygiene, licensing, documentation, CI, and language-specific packaging.

Use it when:

- Making a private repository public
- Auditing an existing public repository for release quality ("make it
- Choosing a license for a project
- Setting up packaging, versioning, or release automation ahead of a public

Do not use it when:

- Routine development on an already-released project (no release event)
- Auditing third-party code for vulnerabilities (use a security-review skill)
- Publishing a package from a repository that will stay private - only the

Requests you can copy:

- **Use:** `Use plugins/development/open-sourcing/skills/open-sourcing/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/open-sourcing/skills/open-sourcing/SKILL.md` | This skill should be used when the user asks to "open source this project", "prepare this repository for public release", "make this repo public", "check open-source readiness", "choose a license for this project", or "set up... | Start here. Say: "Follow plugins/development/open-sourcing/skills/open-sourcing/SKILL.md on this repository." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/aevrin.md` | Aevrin Security Profile: Apply this guidance in addition to the generic workflow when | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/aevrin.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/c-cpp.md` | C/C++ Release Practices: Use modern CMake. For new projects, | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/c-cpp.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/go.md` | Go Release Practices: Use the standard go toolchain for everything. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/go.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/javascript.md` | JavaScript/TypeScript Release Practices: Support the active and maintenance Node.js LTS lines, and declare the floor | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/javascript.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/licensing.md` | Choosing and Applying an Open-Source License: A repository is not open source until it has a license. Without one, default | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/licensing.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/python.md` | Python Release Practices: For project scaffolding, dependency management (uv), formatting/linting | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/python.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/ruby.md` | Ruby Release Practices: Ruby releases a minor version yearly and the community supports roughly the | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/ruby.md before you start." |
| `plugins/development/open-sourcing/skills/open-sourcing/references/rust.md` | Rust Release Practices: Use cargo for everything: building, testing (cargo test), formatting | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/open-sourcing/skills/open-sourcing/references/rust.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/open-sourcing/README.md` | open-sourcing: Prepares a repository for public open-source release. | Human documentation. Read it for install notes and extra details. |

#### review-walkthrough

Folder: [plugins/development/review-walkthrough/](plugins/development/review-walkthrough/)  |  [README](plugins/development/review-walkthrough/README.md)  |  [AGENTS.md](plugins/development/review-walkthrough/AGENTS.md)

Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called.

##### Skill: review-walkthrough

Entry point: `plugins/development/review-walkthrough/skills/review-walkthrough/SKILL.md`

Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called.

Requests you can copy:

- **Use:** `Use plugins/development/review-walkthrough/skills/review-walkthrough/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/review-walkthrough/skills/review-walkthrough/SKILL.md` | Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called. | Start here. Say: "Follow plugins/development/review-walkthrough/skills/review-walkthrough/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/review-walkthrough/README.md` | Review Walkthrough: Generates an interactive HTML walkthrough of committed changes on the current | Human documentation. Read it for install notes and extra details. |

#### second-opinion

Folder: [plugins/development/second-opinion/](plugins/development/second-opinion/)  |  [README](plugins/development/second-opinion/README.md)  |  [AGENTS.md](plugins/development/second-opinion/AGENTS.md)

Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits.

##### Skill: second-opinion

Entry point: `plugins/development/second-opinion/skills/second-opinion/SKILL.md`

Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second opinion on code, a codex review, a gemini review, an antigravity review, or /second-opinion.

Requests you can copy:

- **Use:** `Use plugins/development/second-opinion/skills/second-opinion/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/second-opinion/skills/second-opinion/SKILL.md` | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. Use when the user requests an external review, a second opinion on code, a codex review, a gemini review, an... | Start here. Say: "Follow plugins/development/second-opinion/skills/second-opinion/SKILL.md on this repository." |
| `plugins/development/second-opinion/skills/second-opinion/references/antigravity-invocation.md` | Antigravity Invocation: Use agy print mode with the prepared prompt as one quoted argument. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/second-opinion/skills/second-opinion/references/antigravity-invocation.md before you start." |
| `plugins/development/second-opinion/skills/second-opinion/references/codex-invocation.md` | Codex Invocation: Use codex exec with the prepared prompt on stdin. It supports a | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/second-opinion/skills/second-opinion/references/codex-invocation.md before you start." |
| `plugins/development/second-opinion/skills/second-opinion/references/gemini-invocation.md` | Gemini CLI Invocation: Retain this path for an explicit Gemini CLI request or an account using | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/second-opinion/skills/second-opinion/references/gemini-invocation.md before you start." |
| `plugins/development/second-opinion/skills/second-opinion/references/review-input.md` | Review Input: Use one captured patch and the same review instructions across providers. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/development/second-opinion/skills/second-opinion/references/review-input.md before you start." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/development/second-opinion/README.md` | second-opinion: Get an independent review of uncommitted changes, a branch diff, or a | Human documentation. Read it for install notes and extra details. |

### Team Management

#### team-profile

Folder: [plugins/team-management/team-profile/](plugins/team-management/team-profile/)  |  [README](plugins/team-management/team-profile/README.md)  |  [AGENTS.md](plugins/team-management/team-profile/AGENTS.md)

Interprets Team Profile survey results for individuals and teams

##### Skill: interpreting-team-profile

Entry point: `plugins/team-management/team-profile/skills/interpreting-team-profile/SKILL.md`

Interprets Team Profile (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring profiles, manager coaching, interview transcript analysis for trait prediction, candidate debrief, onboarding planning, and conflict mediation. Accepts extracted JSON or PDF input via OpenCV extraction script. Use when the user shares a Team Profile PDF or JSON profile, asks what someone's CI traits mean, compares Team Profile profiles across a team or against a hiring profile, or asks about burnout risk from Survey-versus-Job gaps.

Use it when:

- Interpreting Team Profile survey results (individual or team)
- Analyzing CI profiles from PDF or JSON data
- Assessing team composition using Gas/Brake/Glue framework
- Detecting burnout risk by comparing Survey vs Job graphs
- Defining hiring profiles based on CI trait patterns
- Coaching managers on how to work with specific CI profiles
- Predicting CI traits from interview transcripts

Do not use it when:

- For non-CI behavioral assessments (DISC, Myers-Briggs, StrengthsFinder, Predictive Index, Enneagram)
- For clinical psychological assessments or diagnoses
- As the sole basis for hiring/firing decisions - CI is one data point among many
- Check same directory as PDF for `.json` file with matching name
- Check if user provided JSON path
- **CI Survey JSON** → Proceed to Step 2
- **CI Survey PDF** → Extract first (Step 0), then proceed to Step 2

Requests you can copy:

- **Use:** `Use plugins/team-management/team-profile/skills/interpreting-team-profile/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/team-management/team-profile/skills/interpreting-team-profile/SKILL.md` | Interprets Team Profile (CI) surveys, behavioral profiles, and personality assessment data. Supports individual profile interpretation, team composition analysis (gas/brake/glue), burnout detection, profile comparison, hiring... | Start here. Say: "Follow plugins/team-management/team-profile/skills/interpreting-team-profile/SKILL.md on this repository." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/anti-patterns.md` | Common mistakes when interpreting Team Profile profiles. Avoiding these errors is as important as understanding the methodology itself. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/anti-patterns.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-administrator.md` | The Administrator (High A, High B, Low C, Mid D): Core: Reasonably proactive, impatient, and amiable communicator. Not strong in the analytical sense, but has the ability to "read" people and situations effectively. Outgoing,... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-administrator.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-coordinator.md` | The Coordinator (Low A, High B, Mid C, Low D): Core: Optimistic, persuasive, socially oriented task facilitator. Sounds assertive and take-charge but is actually an amicable, friendly coordinator who prefers being the... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-coordinator.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-craftsman.md` | The Craftsman (Low A, Low B, High C, High D): Core: Reactive, routine-oriented, and deeply focused on a single task or trade. Gravitates toward the familiar and avoids perceived risk. Predictable, consistent, and highly... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-craftsman.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-daredevil.md` | The Daredevil (High A, Low B, Low C, Low D): Core: Independent, autonomous, take-charge personality with a "No-Fear" mentality. Craves freedom from society, rules, structure, and conformity. Unconventional and uninhibited free... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-daredevil.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-debater.md` | The Debater (Mid A, Mid-High B, Low C, High D): Core: Reasonably assertive and approachable. A friendly, somewhat relaxed person who naturally gravitates to social circles to exchange ideas. Persuasive communicator, usually at... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-debater.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-facilitator.md` | The Facilitator (Low A, Mid B, Mid C, Low D): Core: Polite, cordial, and initially guarded but warms up over time. Easy going and deliberate, excels at single-focus tasks executed in a systematic, methodical way. Socially... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-facilitator.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-influencer.md` | The Influencer (Low A, High B, Low C, Low D): Core: Open, optimistic, unselfish. Comfortable in support roles involving people, service and tasks. Altruistic - finds it hard to say no. Need not to disappoint often puts them... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-influencer.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-operator.md` | The Operator (Low A, Low B, High C, Mid-High D): Core: Easy going, laid back processor of tasks. A creature of habit who prefers stability and predictability. Not a change agent - as steady and consistent as you can get for an... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-operator.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-persuader.md` | The Persuader (High A, High B, Low C, Low D): Core: Proactive, impatient, charismatic communicator. Not strong analytically but has the ability to "read" people and situations effectively. Outgoing, empathetic, and intuitive.... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-persuader.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-philosopher.md` | The Philosopher (Low A, Low B, High C, Low D): Core: Independent, cerebral, idea-driven. Research persistent, strives to stay in a thinking and imaginative environment. A true "ideas" person - out-of-the-box thinking at its... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-philosopher.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-rainmaker.md` | The Rainmaker (High A, High B, Low C, Low D): Core: Assertive, outgoing, socially oriented. Uncanny ability to "read" people despite weak analytical skills. Thrives on putting deals together and has fun doing it. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-rainmaker.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-scholar.md` | The Scholar (High A, Low B, Low C, High D): Core: Somewhat proactive, independent, and research-persistent. Respected for deep knowledge, single focus, and attention span. Relies on information and data from past situations to... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-scholar.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-socializer.md` | The Socializer (Low A, High B, Low C, Low D): Core: Socially flamboyant, people-oriented, and empathetic. Thrives in environments where they can meet, greet, and build relationships. Needs to be seen, heard, and liked - people... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-socializer.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-specialist.md` | The Specialist (Low A, Low B, High C, Mid D): Core: Private, guarded, and introspective. Cannot sit down to watch a movie or relax with friends without a sense of guilt that "there is so much I haven't finished today." Driven... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-specialist.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-technical-expert.md` | The Technical Expert (Low A, Low B, High C, Low D): Core: Impatient, reasonably proactive person who excels in their area of expertise. Driven to be accurate, they will demonstrate their knowledge when given opportunities to... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-technical-expert.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-traditionalist.md` | The Traditionalist (Low A, Low B, High C, High D): Core: Reactive, diligent, detail-oriented individual who draws strength from knowledge and past events. Experts at recalling historic events, people, times, and places.... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-traditionalist.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-trailblazer.md` | The Trailblazer (High A, Mid B, Mid C, Low D): Core: Proactive, confident self-starter that thrives in competitive situations. Focused on winning and driven to be the best at work or hobbies. Tenacious and determined in... | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/archetype-trailblazer.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/conversation-starters.md` | Conversation starters and engagement strategies based on Team Profile traits. Use these to build rapport, deliver feedback effectively, and engage team members based on their profile. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/conversation-starters.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/interview-trait-signals.md` | This reference helps predict Team Profile traits from interview transcripts. Candidates don't take CI during interviews - these signals help estimate traits before the actual survey is administered after an offer is sign | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/interview-trait-signals.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/motivators.md` | The simplest way to drive engagement and productivity is to find the leading dot among A, B, D (the three confidence traits) and install motivators for that trait consistently. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/motivators.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/patterns-archetypes.md` | Team Profile identifies 19 distinct behavioral patterns based on the configuration of A, B, C, D traits. The interaction between traits reveals more than individual positions. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/patterns-archetypes.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/primary-traits.md` | The four primary traits (A, B, C, D) are the main drivers of behavior. The relationship BETWEEN dots is often more important than individual positions. All interpretations are relative to the red arrow (population mean). | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/primary-traits.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/secondary-traits.md` | Secondary traits (EU, L, I) supplement the primary traits. L and I are unique: they use absolute values and CAN be compared directly between people. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/secondary-traits.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/references/team-composition.md` | Every team needs the right mix of Gas, Brake, and Glue for its current needs. The ratio depends on the season of business, the function, and current gaps. | Background and lookup material. Loaded when SKILL.md points to it. Say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/references/team-composition.md before you start." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/templates/burnout-report.md` | Burnout Detection Report Template: Copy and fill this template when analyzing burnout risk using Team Profile Survey vs Job comparison. | Template or example. Say: "Use plugins/team-management/team-profile/skills/interpreting-team-profile/templates/burnout-report.md as the format for the output." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/templates/comparison-report.md` | Profile Comparison Report Template: Copy and fill this template when comparing two Team Profile profiles for compatibility analysis. | Template or example. Say: "Use plugins/team-management/team-profile/skills/interpreting-team-profile/templates/comparison-report.md as the format for the output." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/templates/hiring-profile.md` | Hiring Profile Template: Copy and fill this template when defining the ideal Team Profile profile for a role. | Template or example. Say: "Use plugins/team-management/team-profile/skills/interpreting-team-profile/templates/hiring-profile.md as the format for the output." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/templates/individual-report.md` | Individual Profile Report Template: Copy and fill this template when reporting on an individual's Team Profile profile. | Template or example. Say: "Use plugins/team-management/team-profile/skills/interpreting-team-profile/templates/individual-report.md as the format for the output." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/templates/predicted-profile.md` | Predicted Profile Template: Copy and fill this template when predicting Team Profile traits from interview transcripts. | Template or example. Say: "Use plugins/team-management/team-profile/skills/interpreting-team-profile/templates/predicted-profile.md as the format for the output." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/templates/team-report.md` | Team Composition Report Template: Copy and fill this template when analyzing team composition using Team Profile profiles. | Template or example. Say: "Use plugins/team-management/team-profile/skills/interpreting-team-profile/templates/team-report.md as the format for the output." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/analyze-team.md` | Read these reference files before analyzing: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/analyze-team.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/coach-manager.md` | Read these reference files before coaching: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/coach-manager.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/compare-profiles.md` | Read these reference files before comparing: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/compare-profiles.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/define-hiring-profile.md` | Read these reference files before defining a hiring profile: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/define-hiring-profile.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/detect-burnout.md` | Read these reference files before analyzing: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/detect-burnout.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/extract-from-pdf.md` | Extract from PDF Workflow: Extract Team Profile profile data from a PDF file and convert to JSON format. | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/extract-from-pdf.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/interpret-individual.md` | Read these reference files before interpreting: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/interpret-individual.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/interview-debrief.md` | Read these reference files before debrief: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/interview-debrief.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/mediate-conflict.md` | Read these reference files before mediation: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/mediate-conflict.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/plan-onboarding.md` | Read these reference files before planning onboarding: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/plan-onboarding.md and run that phase." |
| `plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/predict-from-interview.md` | Read these reference files before analyzing: | Step guide for one phase. The skill loads it at that phase. To run it alone say: "Read plugins/team-management/team-profile/skills/interpreting-team-profile/workflows/predict-from-interview.md and run that phase." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/team-management/team-profile/README.md` | Team Profile: Interprets Team Profile survey results for individuals and teams. | Human documentation. Read it for install notes and extra details. |

### Tooling

#### claude-in-chrome-troubleshooting

Folder: [plugins/tooling/claude-in-chrome-troubleshooting/](plugins/tooling/claude-in-chrome-troubleshooting/)  |  [README](plugins/tooling/claude-in-chrome-troubleshooting/README.md)  |  [AGENTS.md](plugins/tooling/claude-in-chrome-troubleshooting/AGENTS.md)

Diagnose and fix Claude in Chrome MCP extension connectivity issues

##### Skill: chrome-mcp-troubleshooting

Entry point: `plugins/tooling/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md`

Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically.

Use it when:

- `mcp__claude-in-chrome__*` tools fail with "Browser extension is not connected"
- Browser automation works erratically or times out
- After updating Claude Code or Claude.app
- When switching between Claude Code CLI and Claude.app (Cowork)
- Native host process is running but MCP tools still fail

Do not use it when:

- **Linux or Windows users** - This skill covers macOS-specific paths and tools (`~/Library/Application Support/`, `osascript`)
- General Chrome automation issues unrelated to the Claude extension
- Claude.app desktop issues (not browser-related)
- Network connectivity problems
- Chrome extension installation issues (use Chrome Web Store support)

Requests you can copy:

- **Use:** `Use plugins/tooling/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md. Task: <describe what you want>. Target: this repository.`

Files in this skill:

| File | What it is | How to use it |
|---|---|---|
| `plugins/tooling/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md` | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extension is not connected", or behave erratically. | Start here. Say: "Follow plugins/tooling/claude-in-chrome-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md on this repository." |

Other files in this plugin:

| File | What it is | How to use it |
|---|---|---|
| `plugins/tooling/claude-in-chrome-troubleshooting/README.md` | Claude in Chrome Troubleshooting: Diagnose and fix Claude in Chrome MCP extension connectivity issues. | Human documentation. Read it for install notes and extra details. |

## Notes

- Skills that run code from the target project need a sandbox with no network access. See [README.md](README.md#requirements).
- Some skills use sub-agents or saved commands. If your agent cannot, it can do the same work step by step. See the table in [AGENTS.md](AGENTS.md).
- Tests and evals inside plugins are for maintainers and are not listed here.
