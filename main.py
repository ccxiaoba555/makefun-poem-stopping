#!/usr/bin/env python3
"""Write an original short poem about stopping to /output/entry.txt.

Deterministic, standard library only, no network access. Running this
program twice produces byte-identical output.
"""

import os

POEM = """The Night the River Rose

The river rose at midnight; I did not run.
I set the kettle down and watched the rain
come sideways over the fence, the garden drowned
in its own reflection, and I stayed.
My neighbor shouted from his truck, engine on,
headlights raking the flood, looking for something to save.
I raised one hand - neither waving him off
nor calling him closer - and held it there.
The dog pressed his warm head to my knee.
Somewhere upstream, a gate gave way; the current
took the fence, the bench, the scarecrow's hat.
I counted my breaths against the rain. One. Two. Three.
The house did not ask to be saved. It asked
to be stood in, feet on the floorboards, listening.
When the water reached the second step, it stopped.
So did I. And in that stopping, I was not nothing -
I was the one thing in the whole wet night
that refused to move just because the water said so.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


def run() -> None:
    main()


if __name__ == "__main__":
    main()
