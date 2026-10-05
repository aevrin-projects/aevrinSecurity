# /// script
# requires-python = ">=3.12"
# dependencies = ["codegraph"]
# ///
"""Generate Mermaid diagrams from Codegraph code graphs.

Thin wrapper — all logic lives in ``codegraph.diagram``.
Run via ``uv run {this_file} --target ... --type ...``.
"""

from __future__ import annotations

import sys

from codegraph.diagram import main

if __name__ == "__main__":
    sys.exit(main())
