import argparse
import sys

def count_lines(text):
    return text.count('\n')

def count_words(text):
    return len(text.split())

def count_chars(text):
    return len(text)

def process_file(file):
    with open(file, 'r') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Python implementation of the wc command")
    parser.add_argument("files", nargs='*', help="Files to be processed")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-c", "--chars", action="store_true", help="Count characters")

    args = parser.parse_args()

    if not args.lines and not args.words and not args.chars:
        args.lines = args.words = args.chars = True

    text = ""
    if args.files:
        for file in args.files:
            text += process_file(file) + "\n"
    else:
        text = sys.stdin.read()

    if args.lines:
        print(f"Lines: {count_lines(text)}")
    if args.words:
        print(f"Words: {count_words(text)}")
    if args.chars:
        print(f"Characters: {count_chars(text)}")

if __name__ == "__main__":
    main()
