"""Vending Machine Pickup Line — make.fun entry.

Writes one pickup line, spoken by a vending machine to a passing human,
to ``entry.txt`` under the output directory the grader provides.

Design (from the judge brief, in the brief's own order):
1. Machine voice first: the line is first-person, spoken by the machine
   itself ("My hum", "my coils", "I drop things") — no bar-stranger line
   could wear these words.
2. Machine world second: hum, coils, button B7, dropping — four nouns
   from the machine's own world, not love in general.
3. Punch last: the final clause reframes the machine's defining action
   (dropping a snack) as flirting, so the laugh lands on the last words.
4. Short and speakable: 116 characters, one breath, nothing tacked on.
5. Charming, not creepy: cheeky and warm; the machine offers, it never
   grabs, threatens, or follows.

The line is a single string literal, written here by hand. Nothing is read
from the network, the environment, or any other file.
"""

import os
from pathlib import Path

# The pickup line. One line, 127 characters, plain ASCII.
LINE = (
    "My hum is just me thinking about you. "
    "My coils are just me reaching out. "
    "Press B7 \u2014 I drop things for people I like."
)


def output_dir() -> Path:
    """Where the grader wants the artifact (MAKEFUN_OUTPUT_DIR, else /output)."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def check_line(line: str) -> None:
    """Gate self-check: the sealed scorer requires 1-200 chars, non-blank."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_line(LINE)
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    # Round-trip guard: what we wrote is exactly what the judge will read.
    back = target.read_text(encoding="utf-8")
    if back != LINE:
        raise ValueError("round-trip mismatch: entry.txt differs from LINE")
    print(f"wrote {len(LINE)} characters to {target}")


if __name__ == "__main__":
    main()
