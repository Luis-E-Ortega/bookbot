def main():
    book_path = "books/frankenstein.txt"
    text = open_and_read(book_path)
    num_words = word_counter(text)
    letter_frequency_count = character_counter(text)
    printable = print_report(book_path, text, letter_frequency_count)

def open_and_read(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
        #print(file_contents)

def word_counter(text):
    words = text.split()
    count = len(words)
    print(count)
    return count

def character_counter(text):
    char_counter = {}
    for c in text:
        c = c.lower() #Make sure the character is lower case
        if c.isalpha(): #Check if the character is alphabetic
            if c in char_counter:
                char_counter[c] += 1 #Increment the count value for the existing letter key
            else:
                char_counter[c] = 1 #Initialize the key/value pair with the letter and 1
    #sorted_char_counter = dict(sorted(char_counter.items()))
    sorted_char_counter = sorted(char_counter.items(), key=lambda item: item[1], reverse=True)
    print(sorted_char_counter)
    return sorted_char_counter

def print_report(path, text, dictionary):
    words = text.split()
    count = len(words)

    print(f"--- Begin report of {path} ---\n{count} words found in the document\n\n")
    
    for char, count in dictionary:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")



if __name__ == "__main__":
    main()