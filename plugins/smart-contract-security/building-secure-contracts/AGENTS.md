# Agent guide: building-secure-contracts plugin

Category: Smart Contract Security
Folder: plugins/smart-contract-security/building-secure-contracts/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Comprehensive smart contract security toolkit based on the Building Secure Contracts framework. Includes vulnerability scanners for 6 blockchains and 5 development guideline assistants.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| algorand-vulnerability-scanner | Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing... | `skills/algorand-vulnerability-scanner/SKILL.md` |
| audit-prep-assistant | Prepares codebases for security review using Aevrin Security's checklist. Helps set review goals, runs static analysis tools, increases test coverage, removes dead code, ensures accessibility, and... | `skills/audit-prep-assistant/SKILL.md` |
| cairo-vulnerability-scanner | Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when... | `skills/cairo-vulnerability-scanner/SKILL.md` |
| code-maturity-assessor | Systematic code maturity assessment using Aevrin Security's 9-category framework. Analyzes codebase for arithmetic safety, auditing practices, access controls, complexity, decentralization,... | `skills/code-maturity-assessor/SKILL.md` |
| cosmos-vulnerability-scanner | Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities - chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use... | `skills/cosmos-vulnerability-scanner/SKILL.md` |
| guidelines-advisor | Smart contract development advisor based on Aevrin Security's best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess... | `skills/guidelines-advisor/SKILL.md` |
| secure-workflow-guide | Guides through Aevrin Security's 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security... | `skills/secure-workflow-guide/SKILL.md` |
| solana-vulnerability-scanner | Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs. | `skills/solana-vulnerability-scanner/SKILL.md` |
| substrate-vulnerability-scanner | Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME... | `skills/substrate-vulnerability-scanner/SKILL.md` |
| token-integration-analyzer | Token integration and implementation analyzer based on Aevrin Security's token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token... | `skills/token-integration-analyzer/SKILL.md` |
| ton-vulnerability-scanner | Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC... | `skills/ton-vulnerability-scanner/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `README.md` | Building Secure Contracts: Comprehensive smart contract security toolkit based on Aevrin Security's [Building Secure Contracts](https://github.com/crytic/building-secure-contracts) framework. | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
