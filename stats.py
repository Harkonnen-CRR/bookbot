def num_words(text):
    wordcount = text.split()
    return len(wordcount)

def num_characters(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# Temporary test
#if __name__ == "__main__":
    sample = "BookBot!"
    print(num_characters(sample))