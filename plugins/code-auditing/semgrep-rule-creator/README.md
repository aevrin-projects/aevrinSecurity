# Semgrep Rule Creator

Create production-quality Semgrep rules for detecting bug patterns and security vulnerabilities.

**Author:** Aevrin Security

## Skills Included

| Skill                 | Purpose                                              |
|-----------------------|------------------------------------------------------|
| `semgrep-rule-creator` | Guide creation of custom Semgrep rules with testing |

## When to Use

Use this skill when you need to:
- Create custom Semgrep rules for detecting specific bug patterns
- Write rules for security vulnerability detection
- Build taint mode rules for data flow analysis
- Develop pattern matching rules for code quality checks

## What It Does

- Guides test-driven rule development (write tests first, then iterate)
- Analyzes AST structure to help craft precise patterns
- Supports both taint mode (data flow) and pattern matching approaches
- Includes comprehensive reference documentation from Semgrep docs
- Provides common vulnerability patterns by language

## Prerequisites

- [Semgrep](https://semgrep.dev/docs/getting-started/) installed (`uv tool install semgrep` or `brew install semgrep`)

## Installation

```
cp -r plugins/code-auditing/semgrep-rule-creator/skills/* <your-agent-skills-dir>/
```

Then run `/semgrep-rule-creator:semgrep-rule` to walk through building a rule.

```
```

## Related Skills

- `semgrep-rule-variant-creator` - Port existing Semgrep rules to new target languages
- `static-analysis` - General static analysis toolkit with Semgrep, CodeQL, and SARIF parsing
- `similar-bug-finder` - Find similar vulnerabilities across codebases
