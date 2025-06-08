"""
Tests for advanced features of the B2A translator.

This module contains tests for numbers, punctuation, and special characters.
"""

import unittest
from b2a.translator import text_to_braille, braille_to_text, BRAILLE_NUMBERS, CAPITAL_INDICATOR, NUMBER_INDICATOR

class TestAdvancedFeatures(unittest.TestCase):
    """Test cases for advanced features like numbers and punctuation."""
    
    def test_numbers_grade1(self):
        """Test converting numbers to Grade 1 Braille and back."""
        # Test individual digits
        for digit in '0123456789':
            braille_digit = BRAILLE_NUMBERS[digit]
            self.assertEqual(text_to_braille(digit, grade=1), f'{NUMBER_INDICATOR}{braille_digit}')
            self.assertEqual(braille_to_text(f'{NUMBER_INDICATOR}{braille_digit}', grade=1), digit)
        
        # Test multi-digit numbers
        test_cases = [
            ('123', f'{NUMBER_INDICATOR}⠂⠆⠒'),
            ('42', f'{NUMBER_INDICATOR}⠲⠆'),
            ('1001', f'{NUMBER_INDICATOR}⠂⠴⠴⠂')
        ]
        
        for number, expected_braille in test_cases:
            self.assertEqual(text_to_braille(number, grade=1), expected_braille)
            self.assertEqual(braille_to_text(expected_braille, grade=1), number)
    
    def test_punctuation_grade1(self):
        """Test converting punctuation to Grade 1 Braille and back."""
        # Test cases for common punctuation
        test_cases = {
            ',': '⠂', ';': '⠆', ':': '⠒',
            '.': '⠲', '!': '⠖', '?': '⠦',
            '(': '⠶', ')': '⠶',
            "'": '⠄', '-': '⠤', '/': '⠌',
            '\\': '⠡', '&': '⠯',
            '+': '⠐⠖',
            '<': '⠐⠂',  # Less than
            '>': '⠐⠆',  # Greater than
            '*': '⠐⠦',
            '=': '⠶⠶',
            '#': '⠼',
            '"': '⠦⠴',  # Double quote
            '$': '⠈⠎',
            '%': '⠨⠴',
            '@': '⠈',
            '[': '⠨⠣', ']': '⠨⠜',
            '{': '⠨⠷', '}': '⠨⠾',
            '_': '⠠⠤',
            '^': '⠘',
            '~': '⠈'
        }
        
        for char, braille in test_cases.items():
            with self.subTest(char=char, braille=braille):
                # Test text to Braille
                result = text_to_braille(char, grade=1)
                self.assertEqual(result, braille, 
                               f'Failed for character: {char} (expected {braille}, got {result})')
                
                # Skip testing Braille to text for multi-character Braille in this test
                if len(braille) == 1:
                    # For number sign, we expect it to be handled specially
                    if char == '#':
                        continue
                        
                    # For parentheses, they map to the same Braille character
                    if char in '()':
                        self.assertIn(braille_to_text(braille, grade=1), '()')
                    # For @ and ~, they map to the same Braille character
                    elif char in '@~':
                        self.assertIn(braille_to_text(braille, grade=1), '@~')
                    else:
                        self.assertEqual(braille_to_text(braille, grade=1), char)
    
    def test_mixed_content_grade1(self):
        """Test mixed content with letters, numbers, and punctuation in Grade 1."""
        test_cases = [
            ("Hello, World!", f"{CAPITAL_INDICATOR}⠓⠑⠇⠇⠕⠂ ⠺⠕⠗⠇⠙⠖"),
            (f"1 + 1 = 2", f"{NUMBER_INDICATOR}⠂ ⠐⠖ {NUMBER_INDICATOR}⠂ ⠶⠶ {NUMBER_INDICATOR}⠆"),
            ("Special chars: #$%&*()", "⠎⠏⠑⠉⠊⠁⠇ ⠉⠓⠁⠗⠎⠒ ⠼⠈⠎⠨⠴⠯⠐⠦⠶⠶")
        ]
        
        for text, expected_braille in test_cases:
            with self.subTest(text=text, expected=expected_braille):
                result = text_to_braille(text, grade=1)
                self.assertEqual(result, expected_braille,
                               f'Failed for text: {text}\nExpected: {expected_braille}\nGot:      {result}')
                
                # Test round-trip conversion
                round_trip = braille_to_text(result, grade=1)
                # For the round-trip, we need to normalize the expected result
                # since some characters might be converted differently (e.g., case)
                normalized_text = text.lower()
                normalized_round_trip = round_trip.lower()
                self.assertEqual(normalized_round_trip, normalized_text,
                               f'Round-trip failed for: {text}')

    def test_grade2_features(self):
        """Test Grade 2 specific features."""
        # Test common contractions
        self.assertEqual(text_to_braille('the'), '⠮')
        self.assertEqual(text_to_braille('and'), '⠯')
        self.assertEqual(text_to_braille('for'), '⠿')
        self.assertEqual(text_to_braille('with'), '⠾')
        
        # Test capital indicators
        self.assertEqual(text_to_braille('Hello'), f'{CAPITAL_INDICATOR}⠓⠑⠇⠇⠕')
        self.assertEqual(text_to_braille('HELLO'), f'{CAPITAL_INDICATOR*2}⠓⠑⠇⠇⠕')
        # Test with numbers and text
        self.assertEqual(
            text_to_braille('The answer is 42'),
            '⠞⠓⠑ ⠁⠝⠎⠺⠑⠗ ⠊⠎ ⠼⠙⠃'
        )
        
        # Test with multiple punctuation
        self.assertEqual(
            text_to_braille('What is this? It\'s a test!'),
            '⠺⠓⠁⠞ ⠊⠎ ⠞⠓⠊⠎⠦ ⠊⠞⠄⠎ ⠁ ⠞⠑⠎⠞⠖'
        )

if __name__ == '__main__':
    unittest.main()
