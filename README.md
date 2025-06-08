# B2A - Braille to Alphabet Translator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A Python-based tool that translates between Braille and the alphabet (and vice versa). This package provides both a Python API and a command-line interface for easy conversion between standard text and Braille.

## Features

- Convert standard text to Braille
- Convert Braille back to standard text
- Simple and intuitive Python API
- Command-line interface for quick conversions
- Comprehensive test suite

## Installation

### From PyPI (coming soon)
```bash
pip install b2a
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
from b2a import text_to_braille, braille_to_text

# Convert text to Braille
braille = text_to_braille("hello world")
print(braille)  # Output: ⠓⠑⠇⠇⠕ ⺃⠕⠗⠇⠙

# Convert Braille to text
text = braille_to_text("⠓⠑⠇⠇⠕ ⺃⠕⠗⠇⠙")
print(text)  # Output: hello world
```

### Command Line Interface

Convert text to Braille:
```bash
b2a --text "hello world"
```

Convert Braille to text:
```bash
b2a --braille "⠓⠑⠇⠇⠕ ⺃⠕⠗⠇⠙"
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
   ```

3. Run tests:
   ```bash
   python -m pytest
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
