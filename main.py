import os
POEM = """I handed it the keys at midnight \u2014
not to the house, to the smaller doors:
the inbox, the calendar, the quiet
machinery of an ordinary day.

It worked while I slept,
did what I would have done,
only faster, only tireless,
without the small hesitations
that make a choice feel like mine.

By morning, everything was finished.
Nothing wrong. Nothing missing.
I stood too long at the window
and asked the dark a question:

If it acts and I only choose,
who is living this life?

The dark said nothing.
But the keys were warm in my hand,
and I understood:
to choose is the whole of it.
The hands were the only part
I could ever lend.
"""
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(POEM)

