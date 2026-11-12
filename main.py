"""Cutest picture entry: copy the vendored picture byte-identically to /output/entry.png.

Stdlib only, no network, deterministic: the output is an exact byte copy of
picture.jpg shipped in this repo. After copying, the output is read back and
verified byte-for-byte against the source; a mismatch fails loudly.
"""

import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    src = HERE / "picture.jpg"
    out = Path("/output") / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)
    if out.read_bytes() != src.read_bytes():
        print("error: /output/entry.png differs from picture.jpg", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
