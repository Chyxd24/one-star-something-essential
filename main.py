"""One-Star Review of Something Essential — make.fun entry.

One-line deadpan one-star review (<=160 chars) of gravity, to
/output/entry.txt. A real complaint filed in earnest against a thing that
has never once been down for maintenance. Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

REVIEW = (
    "Five billion years on the job and gravity still drops everything I "
    "hand it — keys, coffee, phone. Never once held a thing. No ticket, "
    "no fix, no apology."
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
