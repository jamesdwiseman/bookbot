def count_words(book_text):
    text = book_text
    num_words = len(text.split())
    print(f"{num_words} words found in the document")