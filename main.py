import os

# One-star review of an everyday essential: gravity.
# Deadpan complaint filed in earnest against something that cannot be fixed.
ESSENTIAL = "gravity"
REVIEW = (
    "Five billion years on the job and gravity still can't keep anything "
    "where I put it — drops my keys, my coffee, my phone, every single time."
)


def build() -> str:
    return REVIEW


if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    line = build()
    assert 1 <= len(line) <= 160, f"entry too long: {len(line)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote /output/entry.txt ({len(line)} chars)")
