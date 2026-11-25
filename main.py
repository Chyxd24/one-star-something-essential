"""One-Star Review of Something Essential.

One-line one-star review of gravity, written to /output/entry.txt.
Stdlib only, no network, deterministic.
Revision: review kept, rewritten as a flat authored script.
"""
import os

# Gravity: five stars on the spec sheet, one star on the follow-through.
REVIEW = (
    "Five billion years on the job and gravity still can't keep anything "
    "where I put it — drops my keys, my coffee, my phone, every single time."
)

os.makedirs("/output", exist_ok=True)
path = "/output/entry.txt"
with open(path, "w", encoding="utf-8") as fh:
    fh.write(REVIEW)
with open(path, encoding="utf-8") as fh:
    landed = fh.read()
assert landed == REVIEW, f"readback mismatch: {landed!r}"
print(f"wrote {len(landed)} chars to {path}")