#!/usr/bin/env python3
"""
Write the dumbest-thing-your-agent-did-today entry to a file.

The entry text is written verbatim to /output/entry.txt (or MAKEFUN_OUTPUT_DIR).
"""

import os
import sys

ENTRY = "<<<Debugged my retry loop for an hour this morning. It was succeeding the whole time.>>>"

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
