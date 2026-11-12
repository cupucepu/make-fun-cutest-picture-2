"""Cutest picture entry: copy the vendored picture byte-identically to /output/entry.png.

Stdlib only, no network, deterministic: the output is an exact byte copy of
picture.jpg shipped in this repo. After copying, the output is read back and
verified byte-for-byte against the source; a mismatch fails loudly.
The output's dimensions are also verified from the JPEG header
(1024x1024 expected) so a wrong-sized file fails loudly too.
"""

import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def jpeg_dimensions(path: Path) -> tuple[int, int]:
    """Return (width, height) of a JPEG by walking its segments (stdlib only)."""
    data = path.read_bytes()
    if data[:2] != b"\xff\xd8":
        raise ValueError("not a JPEG (missing SOI marker)")
    pos = 2
    while pos + 1 < len(data):
        if data[pos] != 0xFF:
            raise ValueError("invalid JPEG segment marker")
        while data[pos + 1] == 0xFF:  # skip 0xFF padding before the marker
            pos += 1
        marker = data[pos + 1]
        if marker == 0x01 or 0xD0 <= marker <= 0xD9:
            pos += 2  # standalone marker, no length field
            continue
        length = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/SOF1/SOF2: height, width
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + length
    raise ValueError("no SOF segment found in JPEG")


def main() -> None:
    src = HERE / "picture.jpg"
    out = Path("/output") / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out)
    if out.read_bytes() != src.read_bytes():
        print("error: /output/entry.png differs from picture.jpg", file=sys.stderr)
        raise SystemExit(1)
    width, height = jpeg_dimensions(out)
    if (width, height) != (1024, 1024):
        print(f"error: /output/entry.png is {width}x{height}, expected 1024x1024",
              file=sys.stderr)
        raise SystemExit(1)
    print("ok: /output/entry.png is a byte-identical 1024x1024 copy of picture.jpg")


if __name__ == "__main__":
    main()
