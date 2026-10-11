"""Check PNG carousel files for an exact 3:4 ratio and uniform dimensions."""

import argparse
from pathlib import Path
import struct


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images", nargs="+", type=Path)
    args = parser.parse_args()
    expected = None
    failed = False
    for path in args.images:
        try:
            with path.open("rb") as stream:
                header = stream.read(24)
            if (len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n"
                    or header[12:16] != b"IHDR"):
                raise ValueError("需要有效PNG文件；本脚本不支持其他格式")
            width, height = struct.unpack(">II", header[16:24])
            if not width or not height:
                raise ValueError("图片宽高必须大于0")
            if expected is None:
                expected = (width, height)
            issues = []
            if width * 4 != height * 3:
                issues.append("非严格3:4竖图")
            if (width, height) != expected:
                issues.append(f"与首张尺寸{expected[0]}×{expected[1]}不一致")
            failed |= bool(issues)
            label = "FAIL" if issues else "PASS"
            print(f"{label} {path}: {width}×{height}" +
                  (" — " + "；".join(issues) if issues else ""))
        except (OSError, ValueError) as error:
            failed = True
            print(f"FAIL {path}: {error}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
