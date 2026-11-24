"""Entrypoint for the fortune-cookie-wisdom-for-developers make.fun entry.

Writes the one-line developer fortune to /output/entry.txt.
"""

from pathlib import Path

ENTRY_TEXT = "He who merges on Friday at 5 p.m. will debug on Sunday at dawn."


def main() -> None:
    # Write exactly one line, terminated by a trailing newline.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
