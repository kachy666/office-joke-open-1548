#!/usr/bin/env python3
"""Office Joke Open entry.

Writes a single-line office joke to the entry output path
($ENTRY_OUTPUT, default /output/entry.txt) and prints it.
"""

import os
import sys

JOKE = "Our daily standup has lasted 47 minutes, and not one of us is standing."

MAX_CHARS = 200


def validate(text):
    """Check the gate: 1..200 chars, one line, no surrounding whitespace."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(JOKE)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Round-trip check: what landed on disk must be the joke, byte for byte.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "written entry does not match the joke"
    validate(written)
    print(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
