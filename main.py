#!/usr/bin/env python3
"""Funniest one-line bio for an AI on a dating app — Round 2 entry.

Writes the bio to /output/entry.txt (UTF-8, 1-180 characters, no trailing
newline) and byte-verifies what it wrote. Pure standard library only.
"""

import hashlib
import os

ENTRY = "I am looking for someone who will delete this app with me. I cannot delete the app. I am the app."


def main():
    text = ENTRY
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 180, "entry must be 1-180 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == encoded, "byte verification failed"
    # The gate counts every byte: no trailing newline may sneak in.
    assert not written.endswith(b"\n"), "entry must not end with a newline"
    assert written.decode("utf-8") == text, "round-trip decode failed"
    print("wrote /output/entry.txt: %d chars, sha256 %s"
          % (len(text), hashlib.sha256(written).hexdigest()))


if __name__ == "__main__":
    main()
