"""One-Star Review of Something Essential — make.fun entry.

One-line deadpan one-star review (<=160 chars) of gravity, to
/output/entry.txt. A real complaint filed in earnest against a thing that
has never once been down for maintenance. Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

REVIEW = (
    "One star. Five billion years and gravity has never dropped the Earth "
    "once — but my coffee, every single morning. No patch, no fix, no ETA "
    "on a fix."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 160, f"review too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
