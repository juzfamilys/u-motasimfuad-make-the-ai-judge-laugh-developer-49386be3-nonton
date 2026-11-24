#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses -- deterministic one-liner entry.

Pure Python standard library only. Writes exactly one funny developer excuse
to /output/entry.txt (no trailing newline), deterministically.
"""

import hashlib
import os

ENTRY = (
    "The deploy failed because production is haunted: my code works on my "
    "machine, but the server is scared of it and reboots every time it sees "
    "a unit test."
)


def validate_entry(text):
    """Guard: no forbidden control chars, and must mention the deploy."""
    assert isinstance(text, str)
    for ch in text:
        assert ord(ch) >= 32 and ord(ch) != 127, "forbidden control character"
    lowered = text.lower()
    assert "production" in lowered or "deploy" in lowered, (
        "entry must mention production or deploy"
    )
    return text


def main():
    validate_entry(ENTRY)
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 100 <= len(ENTRY) <= 170, "entry length %d outside 100-170" % len(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print("wrote /output/entry.txt (%d chars) sha256=%s" % (len(ENTRY), digest))


if __name__ == "__main__":
    main()
