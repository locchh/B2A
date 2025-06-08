"""
Command-line interface for the B2A Braille translator.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, TextIO

from b2a import __version__, text_to_braille, braille_to_text

def read_from_file_or_stdin(file_path: Optional[str] = None) -> str:
    """Read input from file or standard input."""
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except FileNotFoundError:
            print(f'Error: File not found: {file_path}', file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f'Error reading file: {e}', file=sys.stderr)
            sys.exit(1)
    else:
        return sys.stdin.read().strip()

def write_to_file_or_stdout(content: str, file_path: Optional[str] = None) -> None:
    """Write content to file or standard output."""
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f'Error writing to file: {e}', file=sys.stderr)
            sys.exit(1)
    else:
        print(content)

def main() -> None:
    """Run the B2A command-line interface."""
    parser = argparse.ArgumentParser(
        description='B2A - A tool for translating between text and Braille.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Examples:
  # Convert text to Braille
  b2a text-to-braille "Hello, World!"
  echo "Hello, World!" | b2a text-to-braille
  b2a text-to-braille -i input.txt -o output.brl
  
  # Convert Braille to text
  b2a braille-to-text "⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙⠖"
  echo "⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠇⠙⠖" | b2a braille-to-text
  b2a braille-to-text -i input.brl -o output.txt
  
  # Interactive mode
  b2a interactive
'''
    )
    
    parser.add_argument('--version', action='version', version=f'B2A {__version__}')
    
    # Add subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Text to Braille command
    text_parser = subparsers.add_parser(
        'text-to-braille',
        help='Convert text to Braille',
        description='Convert text to Braille (Grade 2 by default)'
    )
    text_parser.add_argument('text', nargs='?', help='Text to convert to Braille')
    text_parser.add_argument('-i', '--input', help='Input file (default: stdin)')
    text_parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    text_parser.add_argument('--grade', type=int, choices=[1, 2], default=2,
                           help='Braille grade (1 or 2, default: 2)')
    
    # Braille to Text command
    braille_parser = subparsers.add_parser(
        'braille-to-text',
        help='Convert Braille to text',
        description='Convert Braille to text (supports Grade 1 and 2)'
    )
    braille_parser.add_argument('braille', nargs='?', help='Braille to convert to text')
    braille_parser.add_argument('-i', '--input', help='Input file (default: stdin)')
    braille_parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    braille_parser.add_argument('--grade', type=int, choices=[1, 2], default=2,
                              help='Braille grade (1 or 2, default: 2)')
    
    # Interactive mode
    interactive_parser = subparsers.add_parser(
        'interactive',
        help='Start interactive mode',
        description='Interactive translation mode (type "exit" to quit)'
    )
    interactive_parser.add_argument('--grade', type=int, choices=[1, 2], default=2,
                                  help='Braille grade (1 or 2, default: 2)')
    
    args = parser.parse_args()
    
    if not args.command:
        # If no command provided, show help
        parser.print_help()
        return
    
    try:
        if args.command == 'text-to-braille':
            # Get input from argument, file, or stdin
            if args.text:
                input_text = args.text
            else:
                input_text = read_from_file_or_stdin(args.input)
            
            # Convert to Braille
            result = text_to_braille(input_text, grade=args.grade)
            
            # Write output to file or stdout
            write_to_file_or_stdout(result, args.output)
            
        elif args.command == 'braille-to-text':
            # Get input from argument, file, or stdin
            if args.braille:
                input_braille = args.braille
            else:
                input_braille = read_from_file_or_stdin(args.input)
            
            # Convert to text
            result = braille_to_text(input_braille, grade=args.grade)
            
            # Write output to file or stdout
            write_to_file_or_stdout(result, args.output)
            
        elif args.command == 'interactive':
            print(f'B2A Interactive Mode (Grade {args.grade} Braille)')
            print('Type your text to convert to Braille, or paste Braille to convert to text.')
            print('Type "exit" or press Ctrl+C to quit.\n')
            
            while True:
                try:
                    user_input = input('> ').strip()
                    if user_input.lower() in ('exit', 'quit'):
                        break
                        
                    if not user_input:
                        continue
                        
                    # Try to detect if input is Braille (contains Braille characters)
                    if any(c in '⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿' for c in user_input):
                        # Convert Braille to text
                        result = braille_to_text(user_input, grade=args.grade)
                        print(f'Text: {result}')
                    else:
                        # Convert text to Braille
                        result = text_to_braille(user_input, grade=args.grade)
                        print(f'Braille: {result}')
                        
                except KeyboardInterrupt:
                    print('\nExiting...')
                    break
                except Exception as e:
                    print(f'Error: {e}')
    
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
