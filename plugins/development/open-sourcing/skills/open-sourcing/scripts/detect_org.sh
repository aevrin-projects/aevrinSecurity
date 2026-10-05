#!/usr/bin/env bash
# Detects whether the current repository belongs to an organization with an
# additional guidance profile in references/. Prints the profile name
# ("aevrin" or "generic") to stdout.
set -euo pipefail

AEVRIN_ORGS='aevrin|aevrin-security'

remote_matches_aevrin() {
  git remote -v 2>/dev/null | grep -qiE "github\.com[:/](${AEVRIN_ORGS})/"
}

commits_match_aevrin() {
  git log --format='%ae%n%ce' -n 200 2>/dev/null | grep '@aevrin\.net$' >/dev/null
}

main() {
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "error: not inside a git repository" >&2
    exit 1
  fi

  if remote_matches_aevrin || commits_match_aevrin; then
    echo "aevrin"
  else
    echo "generic"
  fi
}

main "$@"
