import unittest

from textkit import count_sentences, count_word
from textkit.report import format_report, top_words


class CountWordTest(unittest.TestCase):
    def test_counts_each_word(self) -> None:
        self.assertEqual(count_word('사과 배 사과'), {'사과': 2, '배': 1})

    def test_ignores_case(self) -> None:
        self.assertEqual(count_word('Apple apple APPLE'), {'apple': 3})

    def test_empty_text(self) -> None:
        self.assertEqual(count_word(''), {})


class CountSentencesTest(unittest.TestCase):
    def test_counts_each_terminator(self) -> None:
        self.assertEqual(count_sentences('안녕. 뭐해? 좋아!'), 3)

    def test_empty_text(self) -> None:
        self.assertEqual(count_sentences(''), 0)

    def test_no_terminator(self) -> None:
        self.assertEqual(count_sentences('끝이 없는 글'), 0)

    def test_repeated_marks_count_once(self) -> None:
        self.assertEqual(count_sentences('정말?! 그래...'), 2)


class ReportTest(unittest.TestCase):
    def test_top_words(self) -> None:
        self.assertEqual(top_words('a b b c c c', 2), [('c', 3), ('b', 2)])

    def test_ties_keep_first_appearance(self) -> None:
        self.assertEqual(top_words('b a', 2), [('b', 1), ('a', 1)])

    def test_format_report(self) -> None:
        self.assertEqual(format_report('a b b', 2), 'b: 2\na: 1')


if __name__ == '__main__':
    unittest.main()
