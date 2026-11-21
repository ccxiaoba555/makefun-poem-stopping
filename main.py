#!/usr/bin/env python3
"""Write a short poem about stopping to /output/entry.txt.

An entry for the make.fun competition "The poem about stopping":
a poem about agency -- the power of stopping, of restraint, of
waiting, of choosing not to act.

Standard library only. No input, no randomness, no network, no clock
and no environment dependence, so the output is byte-for-byte
identical on every run.
"""

import os

POEM = """\
The Door I Didn't Open

The letter stayed unopened on the table
for three whole days. The stamp, a small blue bird,
kept its wings folded. I watered the plant instead.

The kettle boiled. I watched the steam climb
and thin itself against the window, and let it.
The phone lit up at midnight, once, then dark --
a name I knew, a voice I used to answer.

Outside, the rain went on being rain.
A bus sighed past. A dog slept in a doorway,
dreaming whatever dogs dream when no one calls them.

I put my hand on the doorknob, felt the cool brass,
and took my hand away. Not fear. Not giving up.
Just this: the room stayed mine. The hour stayed mine.
The road could wait. For once, so could I.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
