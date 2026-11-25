"""Funniest One-Line Out-of-Office Reply — make.fun bounty entry.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = "I'm out of office. Your email is currently 47th in line and moving backwards."


def _check_length(text):
    if len(text) < 1:
        raise ValueError("entry is empty: must be 1-160 characters")
    if len(text) > 160:
        raise ValueError(
            f"entry too long: {len(text)} characters, maximum is 160"
        )


def _check_not_blank(text):
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def _check_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (contains a newline)")


def _verify_written(path, expected_bytes):
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} does not match the entry "
            f"({len(actual)} bytes written, {len(expected_bytes)} expected)"
        )


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    _check_length(ENTRY)
    _check_not_blank(ENTRY)
    _check_single_line(ENTRY)
    encoded = ENTRY.encode("utf-8")

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(encoded)
    _verify_written(path, encoded)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
