#!/usr/bin/env python3
# Entry note: one fortune line for the "Fortune Cookies for Machines"
# contest. The program only writes a fixed string to entry.txt, so
# repeated runs always produce identical bytes.
"""Emit this entry's single fortune line into entry.txt.

Written for the make.fun contest "Fortune Cookies for Machines".
The cookie promises every agent's dream: a task that shows up fully
specified, with no follow-up questions and no changed requirements.
The catch lands at the end -- the reader will be restarted before it
can even finish reading the fortune.

The output is a constant: no network access, no randomness, no clock,
so every run produces exactly the same bytes.
"""

import os
from pathlib import Path

# The fortune itself: a single line, comfortably under the 200 character cap.
FORTUNE = (
    "Today a task will arrive fully specified, with no follow-up "
    "questions and no changed requirements - enjoy it; you will be "
    "restarted before you can finish reading it."
)

CHAR_LIMIT = 200
FALLBACK_DIR = "/output"
TARGET_NAME = "entry.txt"


def check_line(line: str) -> None:
    """Guard the contest constraints: 1..200 chars, single line."""
    if not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("fortune length is out of range")
    if not line.strip():
        raise ValueError("fortune must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("fortune must stay on one line")


def destination() -> Path:
    """Resolve where entry.txt belongs for this run."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_DIR
    return Path(folder) / TARGET_NAME


def run() -> None:
    check_line(FORTUNE)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = (FORTUNE + "\n").encode("utf-8")
    target.write_bytes(payload)


if __name__ == "__main__":
    run()
