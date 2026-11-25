"""Write the excuse entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

One line, at most 20 words, 1-140 characters: a gamer texting the boss
to skip work on GTA 6 launch week. Pure standard library only.
"""

import os
from pathlib import Path

LINE = "My dentist moved my root canal to Thursday and the only other slot is in March."


def main():
    # Gate: 1-140 characters, at most 20 words.
    assert 1 <= len(LINE) <= 140, len(LINE)
    assert len(LINE.split()) <= 20, len(LINE.split())
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
