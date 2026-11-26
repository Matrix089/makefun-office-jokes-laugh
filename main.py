"""Make the AI Judge Laugh: Office Jokes entry.

Writes one original line about office life to /output/entry.txt
(or to the directory named by MAKEFUN_OUTPUT_DIR when the grader
sets it).

The joke is the printer: it only ever jams on urgent documents,
which is exactly the behaviour you would expect if it could read.
One specific observation, one twist, no setup wasted. The line is
85 characters, well under the 200-character gate.
"""

import os

ENTRY = "The office printer only jams on urgent documents, which is how I learned it can read."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 200:
        raise SystemExit(f"Entry must be 1 to 200 characters, got {len(entry)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
