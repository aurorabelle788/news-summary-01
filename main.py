"""news-summary-01 entry (Python 3.13, standard library only).

The summary lives in summary.txt beside this file; the program copies it,
byte for byte, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
outside the grader's container). No network, no clock, no randomness:
both runs write the same bytes. The gate allows 1 to 2,000 characters,
so the copy is checked against those bounds before it is written.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = (HERE / "summary.txt").read_text(encoding="utf-8")
    if not 1 <= len(text) <= 2000:
        raise ValueError(f"summary is {len(text)} characters, gate allows 1-2000")
    if not text.strip():
        raise ValueError("summary is only white space")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    target = OUT_DIR / "entry.txt"
    target.write_text(text, encoding="utf-8")
    if target.read_text(encoding="utf-8") != text:
        raise ValueError("written entry does not match the summary")


if __name__ == "__main__":
    main()
