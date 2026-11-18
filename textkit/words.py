"""Word counting."""

import re

WORD = re.compile(r'\w+')


def count_words(text: str) -> dict[str, int]:
    """How often each word appears in the text; case is ignored."""
    counts: dict[str, int] = {}
    for word in WORD.findall(text.lower()):
        counts[word] = counts.get(word, 0) + 1
    return counts
