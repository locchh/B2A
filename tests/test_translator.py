"""
Tests for the B2A translator module.
"""

import unittest
from b2a.translator import text_to_braille, braille_to_text, CAPITAL_INDICATOR

class TestTranslator(unittest.TestCase):
    """Test cases for the translator functions."""
    
    def test_text_to_braille_grade1(self):
        """Test converting text to Grade 1 Braille."""
        # Test basic conversion
        self.assertEqual(text_to_braille('hello', grade=1), '⠓⠑⠇⠇⠕')
        self.assertEqual(text_to_braille('hello world', grade=1), '⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙')
        
        # Test case sensitivity
        self.assertEqual(text_to_braille('HELLO', grade=1), f'{CAPITAL_INDICATOR}⠓{CAPITAL_INDICATOR}⠑{CAPITAL_INDICATOR}⠇{CAPITAL_INDICATOR}⠇{CAPITAL_INDICATOR}⠕')
        
        # Test mixed case
        self.assertEqual(text_to_braille('Hello', grade=1), f'{CAPITAL_INDICATOR}⠓⠑⠇⠇⠕')
    
    def test_braille_to_text_grade1(self):
        """Test converting Grade 1 Braille to text."""
        self.assertEqual(braille_to_text('⠓⠑⠇⠇⠕', grade=1), 'hello')
        self.assertEqual(braille_to_text('⠺⠕⠗⠇⠙', grade=1), 'world')
        
        # Test with capital indicators
        self.assertEqual(braille_to_text(f'{CAPITAL_INDICATOR}⠓⠑⠇⠇⠕', grade=1), 'Hello')
        self.assertEqual(braille_to_text(f'{CAPITAL_INDICATOR*2}⠓⠑⠇⠇⠕', grade=1), 'HELLO')
    
    def test_round_trip_grade1(self):
        """Test round-trip conversion with Grade 1 Braille."""
        test_strings = ['hello', 'world', 'test', 'python', 'braille', 'Hello', 'WORLD']
        for s in test_strings:
            with self.subTest(s=s):
                self.assertEqual(braille_to_text(text_to_braille(s, grade=1), grade=1), s)
    
    def test_invalid_input(self):
        """Test handling of invalid input."""
        with self.assertRaises(TypeError):
            text_to_braille(123)  # Not a string
        with self.assertRaises(TypeError):
            braille_to_text(123)  # Not a string
        with self.assertRaises(ValueError):
            text_to_braille('hello', grade=3)  # Invalid grade
        with self.assertRaises(ValueError):
            braille_to_text('hello', grade=0)  # Invalid grade

class TestGrade2BrailleBasic(unittest.TestCase):
    """Basic test cases for Grade 2 Braille."""
    
    def test_grade2_basic(self):
        """Test basic Grade 2 Braille conversion."""
        # Test that Grade 2 is the default
        self.assertEqual(text_to_braille('the'), '⠮')
        self.assertEqual(text_to_braille('and'), '⠯')
        
        # Test that we can force Grade 1
        self.assertEqual(text_to_braille('the', grade=1), '⠞⠓⠑')
        
        # Test round trip
        self.assertEqual(braille_to_text('⠮'), 'the')
        self.assertEqual(braille_to_text('⠯'), 'and')

if __name__ == '__main__':
    unittest.main()
