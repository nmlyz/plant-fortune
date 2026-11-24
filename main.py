#!/usr/bin/env python3
"""Fortune in a Pot -- submission generator.

Writes one kind, funny fortune for a houseplant to ``entry.txt``
inside OUTPUT_DIR (default ``/output``). The line is a single line of
at most 120 characters: a tiny green flag rises from the plant's soil
one morning, a new shoot claiming the windowsill in its name. The
output is deterministic: running the script twice produces
byte-identical files.
"""

import os
from pathlib import Path

LINE = (
    "A tiny green flag will rise from your soil one morning: "
    "a new shoot, claiming this windowsill in your name."
)

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 120


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-120 characters")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    # The entry is collected by another user, so leave it readable by all.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
