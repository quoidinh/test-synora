"""Sample Python module demonstrating clean, tested code."""

import unittest


class StringUtils:
    """A tiny collection of string helpers."""

    @staticmethod
    def reverse(text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Expected a string")
        return text[::-1]

    @staticmethod
    def is_palindrome(text: str) -> bool:
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]

    @staticmethod
    def word_count(text: str) -> int:
        return len(text.split())


class TestStringUtils(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(StringUtils.reverse("hello"), "olleh")

    def test_is_palindrome(self):
        self.assertTrue(StringUtils.is_palindrome("racecar"))

    def test_word_count(self):
        self.assertEqual(StringUtils.word_count("one two three"), 3)

    def test_reverse_type_error(self):
        with self.assertRaises(TypeError):
            StringUtils.reverse(123)


if __name__ == "__main__":
    unittest.main(verbosity=2)
