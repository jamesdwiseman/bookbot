def count_words(book_text): # creates a funtion that takes on parameter book_text, which is the entire text of the book as a string.
    text = book_text #assigns the book_text parameter to a new variable called text. Actuall unncessary becuase you can just use book_text directly. 
    num_words = len(text.split()) #see below:
    return num_words #returns the total word count back to whoever called the function
#text.split() - The .split() method splits the text string into a list of worlds. By default, it splits on any whitespace (spaces, tabs, newlines). So "Hello worl how are you" becomes ["Hello", "world", "how", "are", "you"]
#len(...) -the len() function counts how many items are in the list. So len(["Hello", "world", "how", "are", "you"])  retursn 5.
#num_words = ... - This stores the count in variable num_words

def count_characters(book_text): #create function that takes one paramter book_text, which will be the entire text of the book as a string
    text = book_text.lower() #converts all text to lowercase. You want to count 'A' and 'a' as the same character. Prevent duplicate counting. 
    char_counts = {} #creates empty dictionary that will store each character as a key and its count as teh value. 
    for i in text: #starts loop that goes through every single character in the text string. 
        if i in char_counts: #this checks if the current character i already ecists as a key in the char_counts dictionary. 
            char_counts[i] += 1 #if the character already exists in the dictionary, this adds 1 to its current count.
        else:
            char_counts[i] = 1 #if the character is not already in the dictionary, it creates a new key for that character with a count of 1.
    return char_counts

def sort_on(char_accounts):
    return char_accounts["num"] #this returns the value to sort by

def sorted_characters(char_accounts): # creates function that takes one parameter (char_accounts). 
#Char_accounts is the parameter that will be the dictionary of characters and their counts taht comes from our count_characters function
    sorted_char = [] #create empty list to add dictionary to
    for i in char_accounts:
        char_dict = {} #create dictionary
        char_dict["char"] = i # the character itself
        char_dict["num"] = char_accounts[i] #the count for that character
        sorted_char.append(char_dict) #add the dictionary to the list
    sorted_char.sort(reverse=True, key=sort_on) #sort the list (after the loop ends)
    return sorted_char #return the sorted list
