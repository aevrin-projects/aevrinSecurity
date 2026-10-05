# Team Profile

Interprets Team Profile survey results for individuals and teams.


## When to Use

Use this skill when you need to:
- Interpret an individual's Team Profile profile
- Analyze team composition for gas/brake/glue balance
- Detect burnout signals by comparing Survey vs Job traits
- Compare multiple profiles for compatibility
- Get motivator recommendations for specific trait types

## What It Does

This skill provides expert interpretation of Team Profile behavioral assessments:

- **Relative Interpretation** - Always uses distance from arrow, never absolute values
- **Survey vs Job Analysis** - Identifies behavior modification and energy drain
- **Pattern Recognition** - Maps profiles to 19 archetypes
- **Team Analysis** - Assesses gas/brake/glue balance and gaps
- **Burnout Detection** - Calculates energy utilization and flags risk

## Installation

```
cp -r plugins/team-management/team-profile/skills/* <your-agent-skills-dir>/
```

The plugin ships one skill, `interpreting-team-profile`. It triggers on its own when
you bring it a profile; invoke it directly with
`/team-profile:interpreting-team-profile`.

## Key Concepts

### Trait Colors
| Trait | Color | Measures |
|-------|-------|----------|
| A | Maroon | Autonomy, initiative |
| B | Yellow | Social ability |
| C | Blue | Pace/Patience |
| D | Green | Conformity, detail |
| L | Purple | Logic |
| I | Cyan | Ingenuity |

### Energy Utilization
```
Utilization = (Job EU / Survey EU) x 100

70-130% = Healthy
>130% = STRESS (burnout risk)
<70% = FRUSTRATION (flight risk)
```

### Gas/Brake/Glue Framework
| Role | Trait | Function |
|------|-------|----------|
| Gas | High A | Growth, risk-taking |
| Brake | High D | Quality control |
| Glue | High B | Relationships, morale |

## Input Formats

- **JSON** - Extracted profiles from team-profile tool (recommended)
- **PDF** - Direct PDF analysis using Claude's vision

## Workflows

- `interpret-individual.md` - Single profile analysis
- `analyze-team.md` - Team composition assessment
- `detect-burnout.md` - Stress/frustration detection
- `compare-profiles.md` - Multi-profile compatibility

## Reference Documents

- `primary-traits.md` - A, B, C, D trait details
- `secondary-traits.md` - EU, L, I trait details
- `patterns-archetypes.md` - 19 patterns and archetypes
- `motivators.md` - Engagement strategies by trait
- `team-composition.md` - Gas/brake/glue framework
- `anti-patterns.md` - Common interpretation mistakes
