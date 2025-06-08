"""
B2A (Braille to Alphabet) - A Python package for translating between Braille and the alphabet.

This package provides functionality to translate between standard text and Braille,
supporting both Grade 1 (uncontracted) and Grade 2 (contracted) Braille.
"""

__version__ = '0.2.0'

from .translator import (
    text_to_braille,
    braille_to_text,
    CONTRACTIONS,
    BRAILLE_ALPHABET,
    BRAILLE_NUMBERS,
    BRAILLE_PUNCTUATION,
    CAPITAL_INDICATOR,
    NUMBER_INDICATOR
)

__all__ = [
    'text_to_braille',
    'braille_to_text',
    'CONTRACTIONS',
    'BRAILLE_ALPHABET',
    'BRAILLE_NUMBERS',
    'BRAILLE_PUNCTUATION',
    'CAPITAL_INDICATOR',
    'NUMBER_INDICATOR',
    '__version__'
]
