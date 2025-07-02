import sys
import os
from stats import (
    word_count,
    char_count,
    sorted_dict
)

def get_book_text(path):
   with open(path) as f:
       return f.read()

def print_report(book_path, num_words, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = word_count(text)
    raw_char_counts = char_count(text)
    char_counts = sorted_dict(raw_char_counts)
    print_report(book_path, num_words, char_counts)

main()
