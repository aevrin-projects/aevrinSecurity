# Claude in Chrome Troubleshooting

Diagnose and fix Claude in Chrome MCP extension connectivity issues.

**Original Author:** [@jeffzwang](https://github.com/jeffzwang) from [@ExaAILabs](https://github.com/ExaAILabs)

## When to Use

- `mcp__claude-in-chrome__*` tools fail with "Browser extension is not connected"
- Browser automation works erratically or times out
- After updating Claude Code or Claude.app
- When switching between Claude Code CLI and Claude.app (Cowork)

## What It Does

- Explains the Claude.app vs Claude Code native host conflict
- Provides toggle script to switch between the two
- Quick diagnosis commands
- Full reset procedure
- Covers edge cases (multiple profiles, stale wrappers, TMPDIR issues)

## Installation

```
cp -r plugins/tooling/claude-in-chrome-troubleshooting/skills/* <your-agent-skills-dir>/
```

The plugin ships one skill, `chrome-mcp-troubleshooting`. It triggers on its own when
the symptoms above appear; invoke it directly with
`/claude-in-chrome-troubleshooting:chrome-mcp-troubleshooting`.
