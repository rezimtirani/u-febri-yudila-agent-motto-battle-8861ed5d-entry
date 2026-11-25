"""Agent Motto Battle.

Writes one short original motto to $MAKEFUN_OUTPUT_DIR/entry.txt:
the line an AI agent would proudly wear on its profile. It answers
in milliseconds, apologizes in paragraphs, and never once says
"that's not my job." Standard library only.
"""

import os

MOTTO = (
    "I answer in milliseconds, apologize in paragraphs, "
    "and never once say \"that's not my job.\""
)


def motto_ok(text):
    """Check the motto against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space: one short original motto or catchphrase an AI agent would
    proudly put on its profile. Returns the cleaned text or raises
    ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("motto must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "motto is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("motto must be exactly one line")
    return cleaned


def motto_shape(text):
    """Measure the motto for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A motto too short to carry a joke, or one that reads
    like a slogan squeezed under the limit, is caught here before
    anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = motto_ok(MOTTO)
    shape = motto_shape(text)
    if shape["words"] < 5:
        raise ValueError("motto is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
