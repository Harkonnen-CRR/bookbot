#Import the shit we need
import sys
from stats import num_words, num_characters, sort_chars

#Function Definitions
def get_book_text(filepath):
    with open (filepath) as f:
        return f.read()

def print_report(filepath):
    text = get_book_text(filepath)
    word_count = num_words(text)
    char_counts = num_characters(text)
    sorted_chars = sort_chars(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

#Where the magic happens
def main():
    if len(sys.argv) <2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print_report(filepath)

#Entry Point
if __name__ == '__main__':
        main()