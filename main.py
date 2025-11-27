
from stats import get_num_words
from stats import character_count
from stats import generate_report
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)

    characters = character_count(book_text)

    report = generate_report(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in report:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')
    

main()