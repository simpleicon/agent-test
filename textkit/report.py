"""A short report of the most frequent words."""

from .words import count_words


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """The n most frequent words, most frequent first; ties keep the order of first appearance."""
    counts = count_words(text)
    return sorted(counts.items(), key=lambda item: -item[1])[:n]


def format_report(text: str, n: int = 3) -> str:
    """One "word: count" line per word of top_words."""
    return '\n'.join(f'{word}: {count}' for word, count in top_words(text, n))
