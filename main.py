def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_variable = get_book_text("books/frankenstein.txt")
    count_words(book_variable)

def count_words(book_text):
    text = book_text
    num_words = len(text.split())
    print(f"{num_words} words found in the document")
main()