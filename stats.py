def count_words(book_text):
    text = book_text
    num_words = len(text.split())
    return num_words

def count_characters(book_text):
    text = book_text.lower()
    char_counts = {}
    for i in text:
        if i in char_counts:
            char_counts[i] += 1
        else:
            char_counts[i] = 1
    return char_counts