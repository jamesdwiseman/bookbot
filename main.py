import sys
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
    if len(sys.argv) != 2: #checks if the user provided the wrong number of arguments
     #sys.argv is a list of command line arguments; we want exactly 2 (script name and book path)
        print(f"Usage: python3 main.py <path_to_book>") #if the user did not provide right arguments, show them how to use the program correclty
        sys.exit(1) #stop the program immediately; 1 is an exit code that tells the system the program failed
    book_variable = get_book_text(sys.argv[1])
    result1 = count_words(book_variable) # word count
    result2 = count_characters(book_variable) # character dictionary
    print(f"""============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}...
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