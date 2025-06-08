#!/usr/bin/env python3
"""
Basic usage example of the B2A package.

This script demonstrates how to use the B2A package to convert between
standard text and Braille.
"""

from b2a import text_to_braille, braille_to_text

def main():
    # Example text to convert to Braille
    text = "hello world"
    print(f"Original text: {text}")
    
    # Convert text to Braille
    braille = text_to_braille(text)
    print(f"Braille: {braille}")
    
    # Convert Braille back to text
    converted_back = braille_to_text(braille)
    print(f"Converted back: {converted_back}")
    
    # Verify round-trip conversion
    assert text == converted_back.lower(), "Round-trip conversion failed!"
    print("\nRound-trip conversion successful!")

if __name__ == "__main__":
    main()
