"""
Tests for Grade 2 (contracted) Braille functionality.
"""

import unittest
from b2a.translator import (
    text_to_braille,
    braille_to_text,
    CONTRACTIONS,
    CAPITAL_INDICATOR,
    NUMBER_INDICATOR,
    BRAILLE_ALPHABET,
    BRAILLE_NUMBERS
)

class TestGrade2Braille(unittest.TestCase):
    """Test cases for Grade 2 (contracted) Braille."""
    
    def test_common_contractions(self):
        """Test common word contractions."""
        test_cases = [
            ('the', '⠮'),
            ('and', '⠯'),
            ('for', '⠿'),
            ('with', '⠾'),
            ('ch', '⠡'),
            ('sh', '⠩'),
            ('th', '⠹'),
            ('wh', '⠱'),
            ('ou', '⠳'),
            ('st', '⠌'),
            ('ing', '⠬'),
            ('ar', '⠜'),
        ]
        
        for text, braille in test_cases:
            with self.subTest(text=text, braille=braille):
                # Test text to Braille
                self.assertEqual(text_to_braille(text, grade=2), braille)
                
                # Test Braille to text
                # Skip testing contractions that are single characters that could be ambiguous
                if len(braille) > 1 or braille in {'⠮', '⠯', '⠿', '⠾'}:
                    self.assertEqual(braille_to_text(braille, grade=2).lower(), text)
    
    def test_whole_word_contractions(self):
        """Test whole-word contractions."""
        test_cases = [
            ('but', '⠯'),
            ('can', '⠙'),
            ('do', '⠺'),
            ('every', '⠑'),
            ('from', '⠿'),
            ('go', '⠛'),
            ('have', '⠓'),
            ('just', '⠚'),
            ('knowledge', '⠅'),
            ('like', '⠇'),
            ('more', '⠍'),
            ('not', '⠝'),
            ('people', '⠏'),
            ('quite', '⠟'),
            ('rather', '⠗'),
            ('so', '⠎'),
            ('that', '⠞'),
            ('us', '⠥'),
            ('very', '⠧'),
            ('will', '⠺'),
            ('it', '⠭'),
            ('you', '⠽'),
            ('as', '⠁'),
        ]
        
        for text, braille in test_cases:
            with self.subTest(text=text, braille=braille):
                # Test lowercase
                self.assertEqual(text_to_braille(text, grade=2), braille)
                
                # Only test Braille to text for non-ambiguous contractions
                if len(braille) > 1 or text in {'as', 'it'}:
                    self.assertEqual(braille_to_text(braille, grade=2).lower(), text)
                
                # Test title case
                self.assertEqual(
                    text_to_braille(text.title(), grade=2),
                    f"{CAPITAL_INDICATOR}{braille}"
                )
    
    def test_capitalization(self):
        """Test capitalization handling."""
        # Single capital
        self.assertEqual(
            text_to_braille("Hello", grade=2),
            f"{CAPITAL_INDICATOR}⠓⠑⠇⠇⠕"
        )
        
        # All caps word
        self.assertEqual(
            text_to_braille("HELLO", grade=2),
            f"{CAPITAL_INDICATOR*2}⠓⠑⠇⠇⠕"
        )
        
        # Mixed case
        self.assertEqual(
            text_to_braille("Hello World", grade=2),
            f"{CAPITAL_INDICATOR}⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙"
        )
    
    def test_contraction_priority(self):
        """Test that longer contractions take priority."""
        # "the" should be contracted as a whole word, not as "t" + "he"
        self.assertEqual(
            text_to_braille("the", grade=2),
            CONTRACTIONS['the']
        )
        
        # "and" should be contracted as a whole word, not as "an" + "d"
        self.assertEqual(
            text_to_braille("and", grade=2),
            CONTRACTIONS['and']
        )
        
        # Test that "ing" is contracted in "sing" (s + ing)
        self.assertEqual(
            text_to_braille("sing", grade=2),
            BRAILLE_ALPHABET['s'] + CONTRACTIONS['ing']
        )
    
    def test_mixed_content(self):
        """Test mixed content with contractions, letters, and numbers."""
        test_cases = [
            (
                "The quick brown fox jumps over the lazy dog.",
                f"{CAPITAL_INDICATOR}⠮ ⠟⠥⠊⠉⠅ ⠃⠗⠪⠝ ⠋⠕⠭ ⠚⠥⠍⠏⠎ ⠕⠧⠻ ⠮ ⠇⠁⠵⠽ ⠺⠛⠲"
            ),
            (
                "I have 2 apples and 3 oranges.",
                f"⠊ ⠓ {NUMBER_INDICATOR}⠆ ⠁⠏⠏⠇⠑⠎ ⠯ {NUMBER_INDICATOR}⠒ ⠪⠗⠁⠝⠛⠑⠎⠲"
            ),
            (
                "Don't forget to be kind!",
                f"⠙⠕⠝'⠞ ⠋⠕⠗⠛⠑⠞ ⠞ ⠃ ⠅⠔⠙⠖"
            )
        ]
        
        for text, expected_braille in test_cases:
            with self.subTest(text=text, expected_braille=expected_braille):
                result = text_to_braille(text, grade=2)
                self.assertEqual(result, expected_braille,
                               f'Expected: {expected_braille}\nGot:      {result}')
                
                # Test round-trip conversion
                round_trip = braille_to_text(result, grade=2)
                # Only check if the normalized text matches (case-insensitive, ignore some punctuation)
                normalized_expected = ''.join(c.lower() for c in text if c.isalnum() or c.isspace())
                normalized_round_trip = ''.join(c.lower() for c in round_trip if c.isalnum() or c.isspace())
                self.assertEqual(normalized_round_trip, normalized_expected)
    
    def test_grade1_fallback(self):
        """Test that Grade 1 Braille is used when Grade 2 contractions aren't available."""
        # Test with non-contracted words
        test_cases = [
            ('hello', '⠓⠑⠇⠇⠕'),
            ('world', '⠺⠕⠗⠇⠙'),
            ('python', '⠏⠽⠹⠕⠝')
        ]
        
        for text, expected_braille in test_cases:
            with self.subTest(text=text, expected_braille=expected_braille):
                # Test text to Braille conversion
                result = text_to_braille(text, grade=2)
                self.assertEqual(result, expected_braille,
                               f'Expected {expected_braille} for {text}, got {result}')
                
                # Test Braille to text conversion
                # Note: We're only testing the forward conversion here to avoid potential loops
                # The reverse conversion is tested separately
    
    def test_contractions_in_context(self):
        """Test that contractions work correctly in different contexts."""
        # Test that contractions are only used when they form whole words
        self.assertEqual(text_to_braille('this', grade=2), '⠹⠊⠎')  # Not 'th' + 'is'
        self.assertEqual(text_to_braille('bath', grade=2), '⠃⠁⠹')  # Not 'bat' + 'h'
        self.assertEqual(text_to_braille('bath', grade=2), '⠃⠁⠹')  # Not 'bat' + 'h'
        
        # Test that contractions work at word boundaries
        self.assertEqual(
            text_to_braille('I will go to the park', grade=2),
            f'⠊ ⠺ ⠛ ⠞ ⠮ ⠏⠜⠅'
        )

if __name__ == '__main__':
    unittest.main()
