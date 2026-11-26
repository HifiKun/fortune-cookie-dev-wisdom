"""Write one original fortune-cookie line for a developer to entry.txt."""

import os

FORTUNE = (
    "The bug you cannot reproduce is teaching you patience; "
    "the one you can reproduce is teaching you humility."
)


def main() -> None:
    text = FORTUNE.strip()
    if (
        not text
        or text != FORTUNE
        or len(text) > 120
        or any(ord(c) < 32 for c in text)
    ):
        raise SystemExit("fortune must be one non-empty line of 1-120 characters")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
