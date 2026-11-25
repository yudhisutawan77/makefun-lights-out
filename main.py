"""One Line, Lights Out — make.fun entry.

Writes a single status update (under 200 characters) to stdout and to
the entry output: $ENTRY_OUT when set (as a file, or as a directory
holding entry.txt), and always to /output/entry.txt, which is what the
sealed gate scorer reads.
"""

import os

ENTRY = "lid closed. your download finished at 9:03pm. nobody came back for it."


def resolve_targets():
    """Return the file paths the entry text should be written to."""
    targets = []
    out = os.environ.get("ENTRY_OUT", "").strip()
    if out:
        if os.path.isdir(out) or out.endswith(os.sep):
            targets.append(os.path.join(out, "entry.txt"))
        else:
            targets.append(out)
    targets.append("/output/entry.txt")
    return targets


def main():
    # The sealed gate only accepts 1-200 characters of non-blank UTF-8.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-200 character gate")
    print(ENTRY)
    for path in dict.fromkeys(resolve_targets()):
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(ENTRY)
        except OSError:
            # One unwritable target must not kill the entry; stdout
            # already carries the text and the other target may work.
            continue


if __name__ == "__main__":
    main()
