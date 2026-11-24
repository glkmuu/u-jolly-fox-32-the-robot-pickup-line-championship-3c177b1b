#!/usr/bin/env python3
"""Write the robot pickup line to the make.fun output directory.

Reads entry.txt next to this script, validates the sealed gate
(UTF-8, exactly one line, 1-200 characters, not only whitespace),
and writes it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic, stdlib only, no network.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.txt"
    try:
        raw = src.read_bytes()
    except FileNotFoundError:
        print("entry.txt not found", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        return 1
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("entry.txt is not valid UTF-8", file=sys.stderr)
        return 1
    # A single trailing newline is a file artifact, not a second line.
    if text.endswith("\n"):
        text = text[:-1]
    if "\n" in text or "\r" in text:
        print("entry.txt must be a single line", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
