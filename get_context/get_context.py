"""
File name: get_context.py
Script name: get_context.py
Description:
Extracts context information from Python files and copies it to the clipboard. The information includes the file's purpose, its classes, functions, and methods.

Usage:
1. Single file, entire text: python get_context.py path/to/file.py
2. Single file with only header: python get_context.py path/to/file.py --header
3. Directory with headers: python get_context.py path/to/directory --directory --header
4. Single file without header: python get_context.py path/to/file.py --no_header

The extracted information can be pasted wherever needed.
"""

import os
import argparse
import pyperclip
from rich import print
from rich.table import Table

from . import utils


def get_context_info(file_path, header_only=False, no_header=False):
    with open(file_path, 'r') as f:
        contents = f.read()
    if header_only:
        info = contents.split('"""')[1]
    elif no_header:
        info = contents.split('"""')[-1].strip()
    else:
        info = contents
    return info


def main():
    parser = argparse.ArgumentParser(description='Extract context information from Python files and copy it to the clipboard.')
    parser.add_argument('file_path', help='Path of the Python file or directory to extract information from.')
    parser.add_argument('--header', action='store_true', help='Copy only the header comment.')
    parser.add_argument('--no_header', action='store_true', help='Omit the header comment.')
    parser.add_argument('--directory', action='store_true', help='Process all files in the directory.')
    args = parser.parse_args()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("File Path")
    table.add_column("Tokens")

    clipboard_text = []

    if args.directory:
        # Process all files in the directory
        files = [f for f in os.listdir(args.file_path) if f.endswith('.py')]
        total_tokens = 0
        for f in files:
            file_info = get_context_info(os.path.join(args.file_path, f), args.header, args.no_header)
            file_tokens = utils.count_tokens(file_info)
            total_tokens += file_tokens
            table.add_row(os.path.join(args.file_path, f), str(file_tokens))
            clipboard_text.append(f'{os.path.join(args.file_path, f)}\n{file_info}')
        info = table
    else:
        # Process a single file
        info = get_context_info(args.file_path, args.header, args.no_header)
        total_tokens = utils.count_tokens(info)
        table.add_row(args.file_path, str(total_tokens))
        clipboard_text.append(f'{args.file_path}\n{info}')
        info = table

    print(info)
    print(f"Total number of tokens: {total_tokens}")
    pyperclip.copy('\n'.join(clipboard_text))


if __name__ == '__main__':
    main()
