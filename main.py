#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line to /output/entry.txt: the error message an AI agent
shows when it runs out of tokens mid-sentence.

The gate the sealed scorer enforces: /output/entry.txt must be UTF-8
text of 1 to 140 characters, not only white space, on a single line.
This program checks that itself before writing, so a bad entry can
never be shipped silently.
"""

import os

ENTRY = "Error: token budget exhausted at word 47 of a 48-word sentence. The conclusion is now available as DLC."

MAX_CHARS = 140


def validate(text: str) -> None:
    """Enforce the competition gate locally: 1-140 chars, one line."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
