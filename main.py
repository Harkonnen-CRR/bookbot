def get_book_text(filepath):
    # we need to tell the function how to find and convert the text
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import num_words

from stats import num_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    char_counts = num_characters(text)
    print(f"{num_words(text)} words found in the document")
    print(char_counts)


main()