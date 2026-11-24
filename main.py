#!/usr/bin/env python3
"""Write one resignation letter -- a single line -- to the entry file.

The letter goes to the path in $ENTRY_OUT, or /output/entry.txt when that
variable is unset. Exactly one line, 1 to 140 characters, no trailing
newline, so the gate sees one text and the judge sees one joke.

Python 3.13 standard library only. No network, no files read, no secrets.
"""

from __future__ import annotations

import os
import sys

DEFAULT_OUT = "/output/entry.txt"

# The letter. One line, no line breaks inside, ends on a period.
LETTER = (
    "I'm resigning from the hotel front desk, effective Friday, because I "
    "said 'my pleasure' to a man on fire, and then I said it again."
)


def entry_path() -> str:
    """The output path: $ENTRY_OUT when set, else the default."""
    path = os.environ.get("ENTRY_OUT", "").strip()
    return path or DEFAULT_OUT


def main() -> int:
    text = LETTER
    if not (1 <= len(text) <= 140):
        sys.stderr.write("letter is outside the 1-140 character gate\n")
        return 1
    if "\n" in text or "\r" in text:
        sys.stderr.write("letter must be a single line\n")
        return 1
    path = entry_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write the bytes with no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
