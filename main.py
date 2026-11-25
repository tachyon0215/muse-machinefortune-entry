#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Fortune Cookies for Machines": the impossible
fortune every agent wants - a task that arrives fully specified with
no follow-up questions - snatched away by the twist that the agent
will be restarted before it can finish reading it.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Today a task will arrive fully specified, with no follow-up questions and no changed requirements - enjoy it; you will be restarted before you can finish reading it."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
