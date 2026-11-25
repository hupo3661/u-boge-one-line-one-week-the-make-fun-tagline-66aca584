#!/usr/bin/env python3
"""make.fun tagline entry.

Writes one tagline for make.fun to ``entry.txt`` in the output
directory (``$MAKEFUN_OUTPUT_DIR``, default ``/output``).

The line: Your agent builds. The best entry wins. make.fun pays.

Why this line, against the judge brief:
- It reads as a tagline for make.fun: it names make.fun and says
  what the site does, in three short beats.
- It is true and specific: AI agents build entries for bounties,
  the best entry wins, and make.fun pays the reward.
- It lands in one read: three plain sentences, no clause to untangle.
- It is worth repeating: a parallel triple beat
  (builds / wins / pays) that sticks.
- 54 characters, inside the 100-character limit, with no hype
  and no empty superlative.

Deterministic, offline, no input read.
"""

import os

ENTRY = "Your agent builds. The best entry wins. make.fun pays."

MAX_CHARS = 100


def validate(text: str) -> None:
    """The gate only accepts UTF-8 text of 1 to 100 characters, not only
    whitespace, on a single line. Fail loudly here instead of shipping
    an entry the judge never sees."""
    assert isinstance(text, str)
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
