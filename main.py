from stats import count_words
from stats import count_characters
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_variable = get_book_text("books/frankenstein.txt")
    result1 = count_words(book_variable)
    result2 = count_characters(book_variable)
    print(result1)
    print(result2)
main()