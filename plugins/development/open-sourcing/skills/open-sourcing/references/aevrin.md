# Aevrin Security Profile

Apply this guidance **in addition to** the generic workflow when
`scripts/detect_org.sh` prints `aevrin`. Everything in this file is
public information; internal process details (credentials, announcement
workflow, release sign-off) live in Aevrin Security's internal documentation,
which the maintainer should consult directly.

## License policy

- **Default to [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)**
  for nearly all projects.
- **Use [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html)** when the
  project would offer a significant advantage to competitors who modify it
  without contributing changes back.
- **Use Creative Commons for non-code work:**
  - [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
    for rulesets (e.g., Semgrep rule packs)
  - [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) for
    publications and informational material (e.g.,
    reports and write-ups)
- When in doubt, confirm with the project manager or an existing open-source
  maintainer before publishing.

Copyright line convention (current year only, no ranges):

```
Copyright (c) 2026 Aevrin Security <ujjwal@aevrin.net>
```

For forks and adopted projects, add this line under the existing copyright
rather than relicensing, unless the changes involve the company's competitive
interests (see the AGPLv3 criterion above).

## Repository location

Official projects live in the Aevrin Security GitHub organization
(see [aevrin.net](https://aevrin.net)). Move personal repositories into the
organization before announcing them.

## Package publishing

Publish under the company's shared accounts so ownership survives individual
departures:

- **PyPI:** add the Aevrin Security organization as an owner of the package.
- **RubyGems:** add the Aevrin Security account as a gem co-owner.
- Prefer **trusted publishing** (OIDC from GitHub Actions) over long-lived
  API tokens on every index that supports it (PyPI, RubyGems, crates.io).

Account access is handled internally; consult the internal documentation
rather than creating parallel accounts.

## Project scaffolding

- **Python:** the `modern-python` skill in this skill base covers the current toolchain: uv, ruff, ty, prek, pdoc, SHA-pinned CI audited by zizmor, trusted publishing with SLSA provenance, and coverage gates.
- Example repository for release automation:
  [pip-audit](https://github.com/pypa/pip-audit/blob/main/.github/workflows/release.yml)
  (Python/trusted publishing).

## Before flipping the repository public

Beyond the generic checklist, Aevrin Security maintainers should:

1. Confirm the license choice with their project manager if it deviates from
   Apache 2.0.
2. Follow the internal public-release checklist and announcement process
   (blog post, social media) documented internally — public release is often
   paired with an announcement, and coordinating that before the repository
   goes public preserves the option.
