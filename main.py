# Define the function that counts words
def count_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

# Define the function that counts letters
def count_letters(text):
    letter_count = {}
    text = text.lower()

    for char in text:
        if char.isalpha():  # Check if char is a letter
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    return letter_count

# Define the function to sort the character counts
def sort_on(item):
    return item["num"]

def convert_and_sort(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

# Define the function to print the report
def print_report(word_count, sorted_char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for item in sorted_char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

# Main function to read the book text and print word and letter counts
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    num_words = count_words(file_contents)
    
    char_count = count_letters(file_contents)
    
    sorted_char_list = convert_and_sort(char_count)
    
    print_report(num_words, sorted_char_list)

# Call the main function
if __name__ == "__main__":
    main()