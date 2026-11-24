# SPDX-License-Identifier: MIT
"""Dad Joke Showdown entry.

Writes a single original dad joke to /output/entry.txt.
The joke is fixed text: one clean pun, delivered straight,
short enough to read aloud at the dinner table.
"""

import os

JOKE = (
    "I told my coffee it was too bitter. "
    "It said, \"I've been ground down my whole life "
    "\u2014 all I ask is a little warmth.\""
)


def main() -> None:
    joke = JOKE.strip()
    # The gate counts every character, so keep the count honest here.
    if not 1 <= len(joke) <= 200:
        raise ValueError(f"joke is {len(joke)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(joke)
    print(f"wrote {len(joke)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
