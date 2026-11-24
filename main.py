"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt.
"""

from pathlib import Path

FORTUNE = (
    "The code you inherit was once someone's masterpiece; "
    "write yours so the next heir calls it the same."
)

OUTPUT = Path("/output/entry.txt")

MAX_CHARS = 120


def checked_fortune() -> str:
    """Return the fortune, refusing anything the gate would refuse.

    The sealed scorer only lets UTF-8 text of 1 to 120 characters,
    not only white space, through to the judge — so the program
    checks its own line the same way before writing it.
    """
    if not FORTUNE.strip():
        raise ValueError("fortune is blank")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise ValueError("fortune must be a single line")
    if len(FORTUNE) > MAX_CHARS:
        raise ValueError(f"fortune is {len(FORTUNE)} characters, over {MAX_CHARS}")
    return FORTUNE


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(checked_fortune(), encoding="utf-8")


if __name__ == "__main__":
    main()
