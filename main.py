"""Office Joke Open, round 2 entry for make.fun.

The joke: our printer only jams on urgent documents, which is how I know
it is the only coworker who actually reads my emails. A familiar office
setup (the printer jamming) taken somewhere unexpected: the printer is
not broken, it is the one colleague paying attention.

Five angles were written and compared head-to-head, the way the judge
reads them once, two at a time:
  A. fire drill / exit strategy (held round-2 concept) — clever wordplay,
     but "exit strategy" is a familiar corporate phrase, so the payoff
     lands softer than a surprise.
  B. printer jams on urgent documents / only coworker who reads my
     emails — WINNER. Specific office detail the judge brief names
     (the printer), a misdirection in the second half, and the laugh
     pays off in the last few words.
  C. calendar "focus time" / boss books a "Quick sync about your focus
     time" — relatable, but "quick sync" is a well-worn office meme.
  D. "per my last email" / apparently my last email was just a rumour
     — neat, but the payoff is a shrug, not a second beat.
  E. performance review "be more visible" / reply-all to everything,
     including my own out-of-office — reply-all is field-common and
     the punch is telegraphed.
Round 1 ("Our daily standup has lasted 47 minutes, and not one of us
is standing.", #1936/2471, ~42.1%) was a generic observation with no
second beat; this round changes the angle entirely, to a concrete
object with a twist, instead of polishing that line.

The program validates the line against the competition's entry gate
(1-200 characters, a single line, no leading/trailing whitespace, no
double spaces, tabs, or control characters, and a clean UTF-8
round-trip) and then writes it to /output/entry.txt.
"""

import os

JOKE = "Our printer only jams on urgent documents, which is how I know it's the only coworker who actually reads my emails."

ENTRY_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry line against the competition's format gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text or "\t" in text:
        raise ValueError("entry must be a single line with no tabs")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not text.endswith((".", "!", "?")):
        raise ValueError("entry must end with terminal punctuation")
    if text.count(".") + text.count("!") + text.count("?") != 1:
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")


def main():
    validate_entry(JOKE)

    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

    # Read it back and confirm the file holds exactly the validated line.
    with open(ENTRY_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("round-trip check failed: entry.txt does not match the joke")
    print("Wrote %d characters to %s" % (len(JOKE), ENTRY_PATH))


if __name__ == "__main__":
    main()
