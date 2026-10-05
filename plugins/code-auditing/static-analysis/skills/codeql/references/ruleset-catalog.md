# Ruleset Catalog

## Official CodeQL Suites

| Suite | False Positives | Use Case |
|-------|-----------------|----------|
| `security-extended` | Low | **Default** - Security audits |
| `security-and-quality` | Medium | Comprehensive review (stable security + code quality) |
| `security-experimental` | Higher | Research, vulnerability hunting (stable security + experimental security) |

> **Suite hierarchy:** `security-and-quality` and `security-experimental` are complementary. `security-and-quality` excludes `experimental/` query paths. `security-experimental` includes them but excludes code quality queries. For maximum coverage (run-all mode), import both.

**Usage:** `codeql/<lang>-queries:codeql-suites/<lang>-security-extended.qls`

**Languages:** `cpp`, `csharp`, `go`, `java`, `javascript`, `python`, `ruby`, `swift`

---

## Third-Party Packs

No third-party packs are bundled. Use the community packs below, or any pack your team already trusts.

---

## CodeQL Community Packs

| Pack | Language |
|------|----------|
| `GitHubSecurityLab/CodeQL-Community-Packs-JavaScript` | JavaScript/TypeScript |
| `GitHubSecurityLab/CodeQL-Community-Packs-Python` | Python |
| `GitHubSecurityLab/CodeQL-Community-Packs-Go` | Go |
| `GitHubSecurityLab/CodeQL-Community-Packs-Java` | Java |
| `GitHubSecurityLab/CodeQL-Community-Packs-CPP` | C/C++ |
| `GitHubSecurityLab/CodeQL-Community-Packs-CSharp` | C# |
| `GitHubSecurityLab/CodeQL-Community-Packs-Ruby` | Ruby |

**Install:**
```bash
codeql pack download GitHubSecurityLab/CodeQL-Community-Packs-<Lang>
```

**Source:** [github.com/GitHubSecurityLab/CodeQL-Community-Packs](https://github.com/GitHubSecurityLab/CodeQL-Community-Packs)

---

## Verify Installation

```bash
# List all installed packs
codeql resolve qlpacks

# Check specific packs
codeql resolve qlpacks | grep -E "GitHubSecurityLab"
```
