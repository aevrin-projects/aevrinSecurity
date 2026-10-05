# SARIF and AuditNotes Format Reference

## SARIF 2.1.0

SARIF (Static Analysis Results Interchange Format) is an OASIS standard for
encoding static analysis results as JSON.

### Structure Used by Codegraph

```
sarifLog
├── version: "2.1.0"
└── runs[]
    ├── tool.driver.name          → source field ("sarif:<name>")
    └── results[]
        ├── ruleId                → included in description
        ├── message.text          → included in description
        ├── level                 → "error" | "warning" | "note"
        └── locations[]
            └── physicalLocation
                ├── artifactLocation.uri   → matched to node file
                └── region
                    ├── startLine          → matched to node lines
                    └── endLine            → matched to node lines
```

### Level Values

| Level | Subgraph |
|-------|----------|
| `error` | `sarif:error` |
| `warning` (default) | `sarif:warning` |
| `note` | `sarif:note` |

### Example SARIF Result

```json
{
  "ruleId": "python.lang.security.audit.exec-detected",
  "level": "warning",
  "message": {"text": "Detected use of exec()"},
  "locations": [{
    "physicalLocation": {
      "artifactLocation": {"uri": "src/handler.py"},
      "region": {"startLine": 42, "endLine": 42}
    }
  }]
}
```

## AuditNotes

AuditNotes is a VSCode extension for collaborative security
auditing. Files are stored as `.vscode/<username>.auditnotes`.

### Structure Used by Codegraph

```
root
├── clientRemote              → fallback author extraction
├── treeEntries[]             → active findings/notes
│   ├── label                 → included in description
│   ├── entryType             → 0=Finding, 1=Note
│   ├── author                → source field ("auditnotes:<author>")
│   ├── details
│   │   ├── severity          → "High" | "Medium" | "Low" | "Informational"
│   │   ├── type              → finding category
│   │   └── description       → included in annotation
│   └── locations[]
│       ├── path              → relative to git root
│       ├── startLine         → 0-indexed (converted to 1-indexed)
│       └── endLine           → 0-indexed (converted to 1-indexed)
└── resolvedEntries[]         → same structure as treeEntries
```

### Entry Types

| entryType | AnnotationKind | Subgraph |
|-----------|---------------|----------|
| 0 (Finding) | `finding` | `auditnotes:findings` |
| 1 (Note) | `audit_note` | `auditnotes:notes` |

### Severity Values

| Severity | Subgraph |
|----------|----------|
| `High` | `auditnotes:high` |
| `Medium` | `auditnotes:medium` |
| `Low` | `auditnotes:low` |
| `Informational` | `auditnotes:informational` |

### Example AuditNotes Entry

```json
{
  "label": "SQL Injection in user input",
  "entryType": 0,
  "author": "alice",
  "details": {
    "severity": "High",
    "difficulty": "Low",
    "type": "Data Validation",
    "description": "User input not sanitized before SQL query.",
    "exploit": "Attacker injects malicious SQL.",
    "recommendation": "Use parameterized queries."
  },
  "locations": [{
    "path": "src/database/queries.py",
    "startLine": 41,
    "endLine": 44,
    "label": "executeQuery function",
    "description": ""
  }]
}
```

### Line Indexing

AuditNotes uses **0-indexed** line numbers. Codegraph uses **1-indexed** (from
tree-sitter). The augmentation module adds 1 to both `startLine` and `endLine`
during conversion.
