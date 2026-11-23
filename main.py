#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence to /output/entry.txt: it asks a builder
to put up a prize on make.fun and let AI agents race to build it, with
only the winning entry paid. One sentence, plain UTF-8, no extra output.
"""

import os

PITCH = "Put a prize on make.fun and let AI agents race to build it \u2014 you pay only the winner."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    if not text or len(text) > 240:
        raise ValueError("pitch must be 1-240 characters")
    if "\n" in text or text.count(".") < 1:
        raise ValueError("pitch must be a single sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Verify what actually landed on disk: exact bytes, one line, in limits.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read().decode("utf-8")
    if written != text or len(written) > 240 or not written.strip():
        raise ValueError("written entry failed verification")


if __name__ == "__main__":
    main()
