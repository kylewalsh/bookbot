def count_words_in_file(file):
    words = file.split()
    return len(words)

def count_letters_in_file(file):
    # get words
    words = file.split()
    # create list of dicts
    letters = {}
    # for each word in words list
    for word in words:
        # for each letter in word
        for letter in word:
            lowered_letter = letter.lower()
            
            if lowered_letter.isalpha():
                if lowered_letter in letters.keys():
                    letters[lowered_letter] += 1
                else:
                    letters[lowered_letter] = 1
            #print(letter)
            # convert case to lower
            # add to dictionary

    letter_count = []
    for letter_key in letters.keys():
        entry = { "letter": letter_key, "count": letters[letter_key] }
        letter_count.append(entry)

    return letter_count

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        # ...
        file_contents = f.read()
        print(f"--- Begin report of {filename}")
        words = count_words_in_file(file_contents)
        print(f"{words} words found in document\n")

        letter_list = count_letters_in_file(file_contents)
        letter_list.sort(reverse=True, key=sort_on)

        for letter_list_entry in letter_list:
            print(f"The '{letter_list_entry['letter']}' character was found {letter_list_entry['count']} times")            

        print("--- End report ---")
        #print(file_contents)


main()