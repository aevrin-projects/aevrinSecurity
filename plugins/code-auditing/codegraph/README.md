# codegraph

**Source code graph analysis for security auditing.** Parses code into queryable graphs of functions, classes, and calls, then uses that structure for diagram generation, mutation testing triage, protocol verification, and differential review.

These skills support Codegraph 0.2.x through the 0.5.0 release line. Prefer
`--language auto`, `codegraph.parse.detect_languages()` (0.3+), and
`QueryEngine.preanalysis()` for the core workflow. Before using features added
in v0.4.0 or v0.5.0, check the installed Codegraph version or probe for the
method/CLI command first.

## Compatibility

Use this guard before relying on version-gated features:

```bash
codegraph --version 2>/dev/null || uv run codegraph --version 2>/dev/null
```

Compare the reported version numerically. If it is `0.4.0` or newer, the
expanded v0.4 feature set is available; `0.5.0` or newer adds the v0.5 set.
If the command is missing or reports an older version, stay on the v0.2-safe
baseline — the `codegraph` skill's Version Gate section has the authoritative
list. (The version CLI itself was added in 0.2.2, so a missing command can
also mean codegraph is not installed at all.)

v0.4.0 adds expanded parser coverage, explicit proxy nodes for unresolved
calls, node origins (`source`, `proxy`, `binary`, `synthetic`), new edge kinds
(`resolves_to`, `type_uses`, `specializes`, `corresponds_to`), subgraph edge
and connection queries, generic/type-reference queries, the native
`codegraph diagram` CLI, and binary graph augmentation via `augment_binary()`.

v0.5.0 adds a PostgreSQL-oriented `sql` parser (with node kinds `schema`,
`table`, `view`, `procedure`), the stable `.codegraph/links.toml`
configuration for declaring cross-language/FFI/RPC/external links
(external endpoints become `proxy.external:<symbol>` nodes), repository
links/proxies/`type_uses` edges for single-language parses, Solidity
entrypoints from parser metadata (visibility/mutability/overridden-by
attributes, interfaces excluded), node attributes in `attack_surface()`
entries, TypeScript constructed-receiver resolution, and C# file-scoped
namespace support. It adds no new `QueryEngine` methods or CLI commands, so
gate v0.5 features on the version number, not `hasattr()`.

## Prerequisites

[Codegraph](https://aevrin.net) ([source](https://aevrin.net)) must be installed:

```bash
uv tool install codegraph
# Python snippets: uv run --with codegraph python -   (a tool env is not importable)
```

## Skills

| Skill | Description |
|-------|-------------|
| `codegraph` | Build and query multi-language source/binary code graphs with pre-analysis passes, version feature gates, proxy nodes, type/reference queries, cross-language link configuration, and structural traversal helpers |
| `slicing-code-context` | Build bounded graph-informed source packets and delegate focused work to constrained subagents |
| `diagramming-code` | Generate Mermaid diagrams from code graphs (call graphs, class hierarchies, complexity heatmaps, data flow); v0.4 native diagram support is feature-gated |
| `crypto-protocol-diagram` | Extract protocol message flow from source code or specs (RFC, ProVerif, Tamarin) into sequence diagrams |
| `mutation-triage` | Triage mutation testing results using graph analysis — classify survived mutants as false positives, missing tests, or fuzzing targets |
| `vector-forge` | Mutation-driven test vector generation — find coverage gaps via mutation testing, then generate Wycheproof-style vectors that close them |
| `graph-evolution` | Compare code graphs at two snapshots to surface security-relevant structural changes text diffs miss |
| `codegraph-review-gate` | Apply PASS/WARN/FAIL/UNKNOWN structural gate rules to branch, PR, fix, or release diffs |
| `mermaid-to-proverif` | Convert Mermaid sequence diagrams into ProVerif formal verification models |
| `audit-augmentation` | Project SARIF, AuditNotes, and v0.4 binary-analysis graph findings onto code graphs as annotations and subgraphs |
| `codegraph-finding-triage` | Triage one finding, SARIF result, AuditNotes annotation, suspicious function, or report excerpt with reachability, taint, privilege-boundary, and blast-radius evidence |
| `codegraph-variant-neighborhood` | Expand one seed issue into graph-derived variant candidates for similar-bug-finder, Semgrep, CodeQL, or manual review |
| `codegraph-summary` | Quick structural overview (auto-detected languages, entry points, dependencies) for vivisect/galvanize |
| `codegraph-structural` | Full structural analysis with all pre-analysis passes (blast radius, taint, privilege boundaries, complexity) |

## Directory Structure

```text
codegraph/
├── plugin.json
├── agents/
│   └── code-slice-worker.md          # Bounded worker, no repository tools.
│                                     # Dispatch as `codegraph:code-slice-worker`
├── README.md
└── skills/
    ├── codegraph/                    # Core graph querying
    ├── slicing-code-context/         # Bounded source slicing and worker delegation
    ├── diagramming-code/             # Mermaid diagram generation
    │   └── scripts/diagram.py
    ├── crypto-protocol-diagram/      # Protocol flow extraction
    │   └── examples/
    ├── mutation-triage/                    # Mutation testing triage
    ├── vector-forge/                 # Mutation-driven test vector generation
    │   └── references/
    ├── graph-evolution/              # Structural diff
    │   └── scripts/graph_diff.py
    ├── codegraph-review-gate/         # Structural review gates
    ├── mermaid-to-proverif/          # Sequence diagram → ProVerif
    │   └── examples/
    ├── audit-augmentation/           # SARIF/AuditNotes integration
    ├── codegraph-finding-triage/      # Single-finding evidence packets
    ├── codegraph-variant-neighborhood/ # Variant candidate neighborhoods
    ├── codegraph-summary/            # Quick overview for vivisect/galvanize
    └── codegraph-structural/         # Full structural analysis
```

## Related Skills

| Skill | Use For |
|-------|---------|
| `mutation-testing` | Guidance for running mutation frameworks (mutator, mutator-sol) — use before mutation-triage for triage |
| `differential-review` | Text-level security diff review — complements graph-evolution's structural analysis |
| `code-understanding` | Deep architectural context before vulnerability hunting |
| `similar-bug-finder` | Search for related candidates after codegraph-finding-triage identifies a repeatable root cause |
