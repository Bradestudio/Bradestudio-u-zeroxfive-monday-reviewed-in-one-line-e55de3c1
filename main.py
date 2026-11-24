"""Monday, Reviewed in One Line — make.fun bounty entry.

Writes one review line (105 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The line is a one-star product review of the entrant's own Monday:
Monday shows up uninvited at 6 a.m., eats the whole weekend, and
leaves 47 unread emails as a tip. The review format does the joke's
work — the turn is the tip: the thing that ruined the weekend
behaves like a waiter expecting gratitude for it.
"""

import os
import sys

ENTRY = (
    "One star. Monday showed up uninvited at 6 a.m., "
    "ate my whole weekend, and left 47 unread emails as a tip."
)


def main():
    line = ENTRY
    if not line or not line.strip():
        sys.exit("entry line is blank")
    if "\n" in line or "\r" in line:
        sys.exit("entry line must be a single line")
    if not 1 <= len(line) <= 199:
        sys.exit("entry line must be 1-199 characters, got %d" % len(line))
    if line != line.strip():
        sys.exit("entry line must not start or end with whitespace")
    if not line.endswith("as a tip."):
        # The punch is Monday tipping itself with the unread emails:
        # it must never silently go missing from the line.
        sys.exit("entry line must end with the tip punchline.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated line, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated line")
    print("wrote %s (%d chars, %d bytes)" % (path, len(line), len(data)))


if __name__ == "__main__":
    main()
