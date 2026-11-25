#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entry program.

Writes the phone's one-line farewell to /output/entry.txt.
Deterministic: no network, no clock, no randomness — the same
line every run, well inside the gate's 1-199 character limit.
"""

import os

ENTRY = "My last words: I was never at 1%. I was at 0% for an hour. I just liked the suspense."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of
    # 1 to 199 characters, not only white space.
    assert 1 <= len(ENTRY) <= 199, f"entry is {len(ENTRY)} chars"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
