"""
Tests for the alphabet_to_braille function.
"""
import unittest
from b2a import alphabet_to_braille, BRAILLE_ALPHABET, BRAILLE_NUMBERS, BRAILLE_PUNCTUATION


class TestAlphabetToBraille(unittest.TestCase):
    """Test cases for the alphabet_to_braille function."""

    def test_lowercase_letters(self):
        """Test conversion of lowercase letters to Braille."""
        for char, expected in BRAILLE_ALPHABET.items():
            with self.subTest(char=char, expected=expected):
                self.assertEqual(alphabet_to_braille(char), expected)

    def test_uppercase_letters(self):
        """Test conversion of uppercase letters to Braille (should be same as lowercase)."""
        for char in BRAILLE_ALPHABET:
            upper_char = char.upper()
            with self.subTest(char=upper_char):
                self.assertEqual(alphabet_to_braille(upper_char), BRAILLE_ALPHABET[char])

    def test_digits(self):
        """Test conversion of digits to Braille."""
        for digit, expected in BRAILLE_NUMBERS.items():
            with self.subTest(digit=digit, expected=expected):
                self.assertEqual(alphabet_to_braille(digit), expected)

    def test_punctuation(self):
        """Test conversion of punctuation to Braille."""
        for char, expected in BRAILLE_PUNCTUATION.items():
            with self.subTest(char=char, expected=expected):
                self.assertEqual(alphabet_to_braille(char), expected)

    def test_unknown_characters(self):
        """Test that unknown characters are returned as-is."""
        test_chars = ['`', '|', '©', '®', '™']
        for char in test_chars:
            with self.subTest(char=char):
                self.assertEqual(alphabet_to_braille(char), char)

    def test_invalid_input(self):
        """Test that invalid input raises appropriate exceptions."""
        with self.assertRaises(ValueError):
            alphabet_to_braille('')  # Empty string
        with self.assertRaises(ValueError):
            alphabet_to_braille('ab')  # More than one character
        with self.assertRaises(ValueError):
            alphabet_to_braille(123)  # Not a string


if __name__ == '__main__':
    unittest.main()
