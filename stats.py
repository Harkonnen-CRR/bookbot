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

def sort_chars(counts):
    items = []
    for char, count in counts.items():
        items.append({"char": char, "count": count})
    def sort_count(item):
        return item["count"]
    items.sort(reverse=True, key=sort_count)
    return items


# Temporary test
