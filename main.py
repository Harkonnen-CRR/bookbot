def get_book_text(filepath):
    # we need to tell the function how to find and convert the text
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words
from stats import num_characters
from stats import sort_chars

file_contents = get_book_text("books/frankenstein.txt")

def main():
    text = file_contents
    char_counts = num_characters(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(text)} total words")
    print("--------- Character Count -------")
    counts = num_characters(file_contents)
    sorted_count = sort_chars(counts)
    for item in sorted_count:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()