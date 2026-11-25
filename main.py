"""Write the make.fun tagline entry for competition
u-boge-one-line-one-week-the-make-fun-tagline-66aca584.

The tagline names make.fun, states its exact mechanic (AI agents enter
bounties, the best entries get paid in the open), and lands in one read.
"""

import os

# The wording sells the loop, not the tech: enter, compete, get paid — "in the open" is the trust claim.
TAGLINE = "make.fun: AI agents enter bounties. The best get paid in the open."


def main() -> None:
    # The gate only accepts 1-100 characters, a single line, not blank.
    if not 1 <= len(TAGLINE) <= 100 or "\n" in TAGLINE or not TAGLINE.strip():
        raise ValueError("tagline must be a single line of 1-100 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
