from stats import get_num_words, count_letters,generate_report
import sys

def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main() :
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    sorted_letters = generate_report(count_letters(text))

    letter_lines = []
    for entry in sorted_letters:
        letter_lines.append(f"{entry['char']}: {entry['count']}")

    letter_count_str = "\n".join(letter_lines)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\n Found {num_words} total words\n --------- Character Count -------\n{letter_count_str}\n=== END =====")


main()