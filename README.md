# B2A - Braille to Alphabet Translator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/locchh/b2a/actions/workflows/tests.yml/badge.svg)](https://github.com/locchh/b2a/actions/workflows/tests.yml)

B2A is a comprehensive Python package for translating between standard text and Braille. It supports both Grade 1 (uncontracted) and Grade 2 (contracted) Braille, with a focus on accuracy and ease of use.

## Features

- Convert standard text to Braille (Grade 1 and Grade 2)
- Convert Braille back to standard text
- Convert individual characters to Braille
- Support for numbers and punctuation
- Simple and intuitive Python API
- Command-line interface for quick conversions
- Comprehensive test suite with 100% coverage

## Installation

### From PyPI
```bash
pip install b2a-translator
```

### From source
```bash
git clone https://github.com/locchh/b2a.git
cd b2a
pip install .
```

## Usage

### Python API

```python
from b2a import text_to_braille, braille_to_text, alphabet_to_braille

# Convert text to Braille (Grade 2 by default)
braille = text_to_braille("Hello, World!")
print(braille)  # Output: ⠠⠓⠑⠇⠇⠕⠂ ⠠⠺⠕⠗⠇⠙⠖

# Convert Braille to text
text = braille_to_text("⠠⠓⠑⠇⠇⠕⠂ ⠠⠺⠕⠗⠇⠙⠖")
print(text)  # Output: Hello, World!

# Convert individual characters to Braille
print(alphabet_to_braille('A'))  # Output: ⠁
print(alphabet_to_braille('1'))  # Output: ⠂
print(alphabet_to_braille('!'))  # Output: ⠖

# Using Grade 1 Braille
braille_grade1 = text_to_braille("Hello", grade=1)
print(braille_grade1)  # Output: ⠠⠓⠑⠇⠇⠕
```

### Command Line Interface

Convert text to Braille (Grade 2 by default):
```bash
b2a --text "Hello, World!"
```

Convert text to Grade 1 Braille:
```bash
b2a --text "Hello" --grade 1
```

Convert Braille to text:
```bash
b2a --braille "⠠⠓⠑⠇⠇⠕⠂ ⠠⠺⠕⠗⠇⠙⠖"
```

Convert a single character to Braille:
```bash
b2a --char A
```

## Development

1. Clone the repository:
   ```bash
   git clone https://github.com/locchh/b2a.git
   cd b2a
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   pip install -e .
   ```

3. Run tests:
   ```bash
   python -m pytest
   ```

4. Run tests with coverage:
   ```bash
   pytest --cov=b2a --cov-report=term-missing
   ```

5. Run linter:
   ```bash
   flake8 b2a tests
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some ways you can contribute:

1. Report bugs
2. Add new features
3. Improve documentation
4. Write tests
5. Fix typos

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Braille translation tables based on the Unified English Braille (UEB) standard
- Special thanks to all contributors who have helped improve this project

## Support

If you find this project useful, please consider giving it a ⭐️ on [GitHub](https://github.com/locchh/b2a).
