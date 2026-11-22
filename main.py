"""news-image-20261122: Sunday 22 November 2026's world news in one image.

The image itself lives in this repository as entry.png. This program's
only job is to place a copy of it where the judge looks: /output/entry.png.
It uses nothing but the Python 3.13 standard library, touches no network,
and writes the same bytes on every run: the file is copied, never redrawn,
so the two graded runs always agree. The image is 1024x1024 and under
1 MiB, inside the competition's limits.

Locally, /output does not exist, so MAKEFUN_OUTPUT_DIR stands in for it:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

ENTRY = "entry.png"
DEFAULT_OUTPUT = "/output"


def main() -> None:
    source = Path(__file__).resolve().parent / ENTRY
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / ENTRY)


if __name__ == "__main__":
    main()
