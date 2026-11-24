#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation to /output/entry.txt.

Line 1 explains one everyday thing (a traffic jam) to a 10-year-old in a
single vivid sentence built on one analogy: a giant ketchup bottle.
Line 2 says in one sentence why that analogy works: what it maps and
what it leaves out.

Pure Python standard library; no network, no secrets, no input files.
The output is deterministic so both grader runs produce the same entry.
"""

import os

LINE_1 = (
    "A traffic jam is a giant ketchup bottle held upside down, "
    "with a hundred cars all squeezing to drip out of its narrow neck at once."
)

LINE_2 = (
    "It maps the long wait and the slow squeeze through one narrow opening, "
    "but it leaves out that drivers can turn off and take another road, "
    "while ketchup has nowhere else to go."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    # Gate self-check, mirroring the competition rules: UTF-8 text of
    # 1 to 400 characters, not only white space, exactly two lines.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, must be 1-400"
    assert text.strip(), "entry must not be only white space"
    lines = text.strip().split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "neither line may be blank"
    # Each line must be exactly one sentence: a single terminal period,
    # no other sentence terminators crowding the line.
    for line in lines:
        stripped = line.strip()
        assert stripped.endswith("."), "each line must end with a period"
        assert stripped.count(".") == 1, "each line must hold one sentence"
        assert not any(c in stripped for c in "!?;"), "no extra terminators"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)
    print(f"wrote {len(encoded)} bytes, {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
