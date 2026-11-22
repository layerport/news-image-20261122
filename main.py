#!/usr/bin/env python3
"""World news in one image — 22 November 2026.

Copies the entry image (entry.png, next to this file) to the output
directory as entry.png. Standard library only, deterministic.
"""

import os
import shutil

# No network, no randomness: the same bytes every run.
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
