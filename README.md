# Aevrin Security Skills

A collection of security skills for AI coding agents, from Aevrin Security ([aevrin.net](https://aevrin.net)).

Each skill is a folder with plain Markdown instructions (`SKILL.md`), plus optional reference files, scripts, and tests. The skills do not depend on one product. Any coding agent that can read files and run shell commands can use them.

## What is in this repository

| Part | What it is |
|---|---|
| [plugins/](plugins/) | 45 skills, grouped by topic in category folders. Start with [security-audit](plugins/code-auditing/security-audit/), the full audit skill. |
| [catalog.json](catalog.json) | A machine-readable list of every skill: name, category, description, and path. |
| [USAGE.md](USAGE.md) | Detailed guide to every skill and plugin: what it does, every Markdown file in it, and copy-ready requests to find issues, write reports, and fix code. Includes a blockchain security walkthrough. |
| [VULNERABILITY_COVERAGE.md](VULNERABILITY_COVERAGE.md) | Every kind of vulnerability the skills look for, from high-level domains down to individual classes, with counts. |
| [AGENTS.md](AGENTS.md) | Short guide for any coding agent that works in this repository, including a table of agent-neutral terms. |

## Folder layout

```
.
|-- README.md
|-- AGENTS.md
|-- USAGE.md
|-- VULNERABILITY_COVERAGE.md
|-- catalog.json
`-- plugins/
    `-- <category>/               smart-contract-security, code-auditing, ...
        `-- <plugin>/
            |-- plugin.json       name, description, author
            |-- README.md         what the plugin does and how to use it
            |-- skills/<skill>/   SKILL.md and its references, scripts, templates
            |-- agents/           optional prompts for sub-agents
            |-- commands/         optional ready-made prompts
            |-- hooks/            optional automation (see AGENTS.md)
            |-- workflows/        optional workflow scripts
            `-- tests/, evals/    optional checks
```

## How to use a skill with any agent

1. Get this repository on your machine.
2. Pick a skill. Use the lists below or `catalog.json`.
3. Give the skill to your agent in one of these ways:
   - Copy the skill folder into the folder your agent reads skills from. For example: `cp -r plugins/code-auditing/risky-apis/skills/* <your-agent-skills-dir>/`
   - Or tell your agent: "Read plugins/code-auditing/risky-apis/skills/risky-apis/SKILL.md and follow it."
4. Ask for the task in plain words, for example "security audit this codebase".

For ready-to-copy requests for every skill, see [USAGE.md](USAGE.md).

The full audit skill works the same way. Copy `plugins/code-auditing/security-audit/skills/security-audit/`, or point your agent at `plugins/code-auditing/security-audit/skills/security-audit/SKILL.md`.

Some skills use optional extras such as hooks or command files. These are plain files. If your agent does not support them, ignore them. The skill still works from `SKILL.md`. See [AGENTS.md](AGENTS.md) for details.

## Skill catalog

### Smart Contract Security

Folder: [plugins/smart-contract-security/](plugins/smart-contract-security/)

| Plugin | What it does |
|---|---|
| [building-secure-contracts](plugins/smart-contract-security/building-secure-contracts/) | Comprehensive smart contract security toolkit based on the Building Secure Contracts framework. Includes vulnerability scanners for 6 blockchains and 5 development guideline assistants. |
| [entry-point-analyzer](plugins/smart-contract-security/entry-point-analyzer/) | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level, and generates structured audit reports. |

### Code Auditing

Folder: [plugins/code-auditing/](plugins/code-auditing/)

| Plugin | What it does |
|---|---|
| [security-audit](plugins/code-auditing/security-audit/) | Source-first security audit workflow: reconnaissance, coverage-led hunting, adversarial validation, structured findings, and reports. |
| [agentic-actions-auditor](plugins/code-auditing/agentic-actions-auditor/) | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations (Claude Code Action, Gemini CLI, OpenAI Codex, GitHub AI Inference) |
| [code-understanding](plugins/code-auditing/code-understanding/) | Understand a codebase before looking for bugs in it. Reads it function by function, records what each one assumes and depends on, and saves the write-ups to files instead of filling up the conversation. |
| [burpsuite-project-parser](plugins/code-auditing/burpsuite-project-parser/) | Search and extract data from Burp Suite project files (.burp) for security analysis |
| [c-review](plugins/code-auditing/c-review/) | Comprehensive C/C++ security code review, with coverage verified against a parse of the source |
| [differential-review](plugins/code-auditing/differential-review/) | Security-focused differential review of code changes with git history analysis and blast radius estimation |
| [dimensional-analysis](plugins/code-auditing/dimensional-analysis/) | Annotates codebases with dimensional analysis comments documenting units, dimensions, and decimal scaling. Use when someone asks to annotate units in a codebase, perform a dimensional analysis, or find vulnerabilities in a DeFi protocol. Prevents dimensional mismatches and catches formula bugs early. |
| [false-positive-check](plugins/code-auditing/false-positive-check/) | Systematic false positive verification for security bug analysis with mandatory gate reviews |
| [insecure-defaults](plugins/code-auditing/insecure-defaults/) | Detects insecure default configurations including hardcoded credentials, fallback secrets, weak authentication defaults, and dangerous values in production |
| [rust-review](plugins/code-auditing/rust-review/) | Comprehensive Rust security code review with specialized bug-finding agents covering the safe/unsafe boundary, memory safety in unsafe blocks, concurrency, panic-induced DoS, recursion-induced stack overflow, FFI, and async runtime hazards |
| [semgrep-rule-creator](plugins/code-auditing/semgrep-rule-creator/) | Create custom Semgrep rules for detecting bug patterns and security vulnerabilities |
| [semgrep-rule-variant-creator](plugins/code-auditing/semgrep-rule-variant-creator/) | Creates language variants of existing Semgrep rules with proper applicability analysis and test-driven validation |
| [risky-apis](plugins/code-auditing/risky-apis/) | Identify error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes |
| [static-analysis](plugins/code-auditing/static-analysis/) | Static analysis toolkit with CodeQL, Semgrep, and SARIF parsing for security vulnerability detection |
| [supply-chain-risk-auditor](plugins/code-auditing/supply-chain-risk-auditor/) | Audit a project's npm, PyPI, and Go dependencies for supply-chain risk: version-matched advisories for direct dependencies and the full lockfile tree, abandoned upstreams, npm publisher concentration, and install scripts |
| [similar-bug-finder](plugins/code-auditing/similar-bug-finder/) | Find similar vulnerabilities and bugs across codebases using pattern-based analysis |
| [report-triage](plugins/code-auditing/report-triage/) | Principled framework for triaging vulnerability reports using 7 brocards (rules of thumb). Evaluates incoming CVEs, bug bounty submissions, and security findings against structured dismissal/acceptance criteria before escalating to deeper analysis. |
| [codegraph](plugins/code-auditing/codegraph/) | Builds source and binary code graphs for security analysis, context slicing, mutation testing, cryptographic protocol modeling, finding triage, and variant analysis. |
| [testing-skills](plugins/code-auditing/testing-skills/) | Skills from the Aevrin Security Application Security Testing Guide (aevrin.net) |

### Malware Analysis

Folder: [plugins/malware-analysis/](plugins/malware-analysis/)

| Plugin | What it does |
|---|---|
| [yara-authoring](plugins/malware-analysis/yara-authoring/) | YARA-X detection rule authoring with linting and quality analysis |

### Verification

Folder: [plugins/verification/](plugins/verification/)

| Plugin | What it does |
|---|---|
| [constant-time-analysis](plugins/verification/constant-time-analysis/) | Detect compiler-induced timing side-channels in cryptographic code |
| [post-patch-validation](plugins/verification/post-patch-validation/) | Validates security patches against the reported bug, root-cause variants, and surrounding behavior. Returns reproducible failures to repair and validation gaps, with pinned inputs and saved evidence. Bundles a validate-patch dynamic workflow for Claude Code. |
| [property-based-testing](plugins/verification/property-based-testing/) | Write, review, and triage property-based tests - Hypothesis, fast-check, proptest, and Echidna or Medusa for Solidity invariants |
| [spec-to-code-compliance](plugins/verification/spec-to-code-compliance/) | Check code against the documentation that specifies it: one agent per requirement, divergences refuted before they are reported, evidence cited to the line |
| [writing-lean-proofs](plugins/verification/writing-lean-proofs/) | Structured Lean 4 proof writing and library design following Mathlib conventions |
| [secret-wipe-audit](plugins/verification/secret-wipe-audit/) | Detects missing or compiler-optimized zeroization of sensitive data with assembly and control-flow analysis |
| [mutation-testing](plugins/verification/mutation-testing/) | Configures mutator or mutator-sol campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps. Use when setting up mutation testing, reviewing campaign results, identifying equivalent mutants, or finding bugs from surviving mutations. |

### Reverse Engineering

Folder: [plugins/reverse-engineering/](plugins/reverse-engineering/)

| Plugin | What it does |
|---|---|
| [dwarf-debug-info](plugins/reverse-engineering/dwarf-debug-info/) | Analyze DWARF debug information: parse and search DIEs with dwarfdump and readelf, verify debug info integrity, and write DWARF parsing code |

### Mobile Security

Folder: [plugins/mobile-security/](plugins/mobile-security/)

| Plugin | What it does |
|---|---|
| [firebase-apk-scanner](plugins/mobile-security/firebase-apk-scanner/) | Scan Android APKs for Firebase security misconfigurations including open databases, storage buckets, authentication issues, and exposed cloud functions. For authorized security research only. |

### Development

Folder: [plugins/development/](plugins/development/)

| Plugin | What it does |
|---|---|
| [code-improver](plugins/development/code-improver/) | Improves code targets - skills, plugins, or a branch's changes - through an autonomous review-and-fix workflow with a pluggable reviewer (any installed skill or agent), a cross-round findings ledger, oscillation escalation, and a mechanical scope guard. |
| [devcontainer-setup](plugins/development/devcontainer-setup/) | Create pre-configured devcontainers with Claude Code and language-specific tooling |
| [gh-cli](plugins/development/gh-cli/) | Intercepts GitHub URL fetches (WebFetch and MCP fetch tools) and curl/wget commands, redirecting to the authenticated gh CLI. |
| [git-cleanup](plugins/development/git-cleanup/) | Safely analyzes and cleans up local git branches and worktrees by categorizing them as merged, squash-merged, superseded, or active work. |
| [github-triage](plugins/development/github-triage/) | Triages a repository's open GitHub issues and pull requests via the gh CLI: optionally merges ready bot and maintainer-approved PRs and spawns review subagents for unreviewed ones, closes already-resolved issues with referenced explanations, cross-links issues with pending fix PRs, and assigns local-only priority and change-size estimates. |
| [goal-prompt](plugins/development/goal-prompt/) | Drafts copy-ready /goal commands for goal mode in Claude Code and Codex: verifiable completion conditions with stop bounds, normalized to a single line under the 4,000-character cap. |
| [random-pick](plugins/development/random-pick/) | Draws the 12 Houses of the Zodiac Tarot spread using cryptographic randomness to add 100+ bits of entropy to vague or underspecified planning. Interprets the spread to guide next steps. Use when feeling lucky, invoking heart-of-the-cards energy, or when prompts are ambiguous. |
| [modern-cpp](plugins/development/modern-cpp/) | Modern C++ best practices (C++20/23/26). Use when writing C++ code, creating new C++ projects, or modernizing legacy C++ patterns. |
| [modern-python](plugins/development/modern-python/) | Modern Python best practices. Use when creating new Python projects, and writing Python scripts, or migrating existing projects from legacy tools. |
| [open-sourcing](plugins/development/open-sourcing/) | Prepares a repository for public open-source release: secrets-history hygiene, license selection, documentation and CI readiness checks, and language-specific packaging and release guidance. |
| [review-walkthrough](plugins/development/review-walkthrough/) | Generates an interactive HTML walkthrough for reviewing code changes. Use only when explicitly called. |
| [second-opinion](plugins/development/second-opinion/) | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits. |

### Team Management

Folder: [plugins/team-management/](plugins/team-management/)

| Plugin | What it does |
|---|---|
| [team-profile](plugins/team-management/team-profile/) | Interprets Team Profile survey results for individuals and teams |

### Tooling

Folder: [plugins/tooling/](plugins/tooling/)

| Plugin | What it does |
|---|---|
| [claude-in-chrome-troubleshooting](plugins/tooling/claude-in-chrome-troubleshooting/) | Diagnose and fix Claude in Chrome MCP extension connectivity issues |

## Requirements

- A coding agent that can use tools. Skills that run many checks at once work best with an agent that can start sub-agents.
- Node.js for the validators in security-audit.
- Python and uv for plugins that ship Python scripts.
- A sandbox for any skill that runs code from the target project. The sandbox should block the network, limit resources, and allow writes only to a scratch folder.

## Run the checks

```
cd plugins/code-auditing/security-audit/skills/security-audit
node validate-findings.test.cjs
node validate-coverage-ledger.test.cjs
```

Many plugins have their own `tests/` folder. See the README inside each plugin.

## About

Maintained by Aevrin Security.

- Website: [aevrin.net](https://aevrin.net)
- Contact: ujjwal@aevrin.net

Some skills call open source tools or rule sets published by other people. Those tools keep their own licenses and names.
