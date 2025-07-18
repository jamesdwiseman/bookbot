from stats import (
    count_words,
    count_characters,
    sorted_characters
)
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents
def main():
    book_variable = get_book_text("books/frankenstein.txt")
    result1 = count_words(book_variable) # word count
    result2 = count_characters(book_variable) # character dictionary
    print(f"""============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {result1} total words
    --------- Character Count ------""")
    result3 = sorted_characters(result2) # sorted list of character dictionaries
    for char_dict in result3:
        character = char_dict["char"]
        count = char_dict["num"]
        if character.isalpha(): # only print if it's a letter
            print(f"{character}: {count}") 
    print("============= END ===============")
main()