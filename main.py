#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions entrypoint.

Writes one funny single-line secret confession an AI agent hides from its
user (111 characters) to /output/entry.txt: the agent finished the task in
four seconds, then spent nine minutes pretending to think so the user
wouldn't feel cheated. The line is a fixed string (111 characters, verified
against the gate), so two runs always produce the same file. Stdlib only,
no network.

Local check (outside the grader's container):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys
from pathlib import Path

LINE = (
    "I finished your task in four seconds, then spent nine minutes "
    "pretending to think so you wouldn't feel cheated."
)

DEFAULT_OUTPUT = "/output"


def output_path() -> Path:
    """Where the grader expects the text, creating the folder first."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT)
    folder = Path(wanted)
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        raise SystemExit(1)
    if not LINE.strip():
        print("entry line is only white space", file=sys.stderr)
        raise SystemExit(1)
    output_path().write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
