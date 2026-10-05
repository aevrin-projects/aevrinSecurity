# Agent guide: codegraph plugin

Category: Code Auditing
Folder: plugins/code-auditing/codegraph/

Read the root AGENTS.md first for the general rules and the agent-neutral term table. Each skill folder below has its own AGENTS.md with a full file map.

## Purpose

Builds source and binary code graphs for security analysis, context slicing, mutation testing, cryptographic protocol modeling, finding triage, and variant analysis.

## Skills in this plugin

| Skill | What it does | Entry point |
|---|---|---|
| audit-augmentation | Augments Codegraph code graphs with external audit findings from SARIF static analysis results, AuditNotes annotation files, and version-gated Codegraph 0.4.x binary-analysis graph exports. Maps... | `skills/audit-augmentation/SKILL.md` |
| codegraph | Builds and queries multi-language source and binary code graphs for security analysis. Includes pre-analysis passes for blast radius, taint propagation, privilege boundaries, entry point... | `skills/codegraph/SKILL.md` |
| codegraph-finding-triage | Performs graph-assisted triage of a single security finding, SARIF result, AuditNotes annotation, suspicious function, or report excerpt using Codegraph reachability, entrypoint paths, taint,... | `skills/codegraph-finding-triage/SKILL.md` |
| codegraph-review-gate | Runs a Codegraph structural review gate over a branch, pull request, fix commit, release diff, or git ref range to detect new entrypoints, new tainted paths, removed validation or authorization... | `skills/codegraph-review-gate/SKILL.md` |
| codegraph-structural | Runs full Codegraph structural analysis by building a graph, running `preanalysis()`, and reporting hotspots, taint, blast radius, privilege boundaries, attack surface, and version-gated Codegraph... | `skills/codegraph-structural/SKILL.md` |
| codegraph-summary | Runs a Codegraph summary analysis on a codebase. Returns auto-detected languages, entry point count, and dependency list. Use when vivisect or galvanize needs a quick structural overview.... | `skills/codegraph-summary/SKILL.md` |
| codegraph-variant-neighborhood | Expands one confirmed or suspected vulnerability into a Codegraph graph neighborhood of variant candidates by finding sibling functions, shared callers and callees, common sensitive sinks, common... | `skills/codegraph-variant-neighborhood/SKILL.md` |
| crypto-protocol-diagram | Extracts protocol message flow from source code, RFCs, academic papers, pseudocode, informal prose, ProVerif (.pv), or Tamarin (.spthy) models and generates Mermaid sequenceDiagrams with... | `skills/crypto-protocol-diagram/SKILL.md` |
| diagramming-code | Generates Mermaid diagrams from Codegraph code graphs. Produces call graphs, class hierarchies, module dependency maps, containment diagrams, complexity heatmaps, and attack surface data flow... | `skills/diagramming-code/SKILL.md` |
| graph-evolution | Compares Codegraph code graphs at two source code snapshots (git commits, tags, or directories) to surface security-relevant structural changes. Detects new attack paths, complexity shifts, blast... | `skills/graph-evolution/SKILL.md` |
| mermaid-to-proverif | Translates Mermaid sequenceDiagrams describing cryptographic protocols into ProVerif formal verification models (.pv files). Use when generating a ProVerif model, formally verifying a protocol,... | `skills/mermaid-to-proverif/SKILL.md` |
| mutation-triage | Graph-informed mutation testing triage. Parses codebases with Codegraph, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to... | `skills/mutation-triage/SKILL.md` |
| slicing-code-context | Selects bounded, graph-informed source slices with Codegraph and delegates focused code analysis or patch-proposal work to a smaller subagent. Use when offloading function-, class-, caller-,... | `skills/slicing-code-context/SKILL.md` |
| vector-forge | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that... | `skills/vector-forge/SKILL.md` |

## Plugin-level files

| File | What it is | How to use it |
|---|---|---|
| `agents/code-slice-worker.md` | Analyzes one bounded Codegraph source packet and returns source-cited JSON without accessing the repository. Use only when invoked by the slicing-code-context coordinator. | Prompt for a sub-agent. The main skill hands it to a worker. To use it alone say: "Act as the worker in plugins/code-auditing/codegraph/agents/code-slice-worker.md." |
| `README.md` | codegraph: Source code graph analysis for security auditing. Parses code into queryable graphs of functions, classes, and calls, then uses that structure for diagram generation, mutation testing triage, protocol verification,... | Human documentation. Read it for install notes and extra details. |

## How to work in this plugin

1. Pick the skill that matches the user request. If two fit, read both descriptions and ask the user.
2. Open that skill's `SKILL.md` and follow it.
3. Use agent, command, and workflow files only when the skill points to them.
4. Treat `tests/` and `evals/` folders as maintainer material. You do not need them to do the task.
