from stats import num_words, num_characters, sort_chars

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

if __name__ == '__main__':
    print_report("books/frankenstein.txt")