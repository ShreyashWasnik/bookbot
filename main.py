def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")
    print("")
    num_words = get_num_words(text)
    print(f"{num_words} were found in the document")
    num_letters = get_num_letters(text)
    final_list = get_num_letters_sorted(num_letters)
    for item in final_list:
        print(f"The {item['char']} character was found {item['num']} times")
    print(f"--- End Report ---")
    




def get_book_text(path):
    with open(path) as f:
        return f.read()



def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    count_letters = {}
    lower = text.lower()
    alphabets = ['a','b','c','d','e','f','g','h',
                 'i','j','k','l','m','n','o','p',
                 'q','r','s','t','u','v','x','y','z']

    for letter in alphabets:
        count = 0
        for t in text:
            if t == letter:
                count += 1
                count_letters[letter] = count
    return count_letters

def sort_on(d):
    return d["num"]

def get_num_letters_sorted(num_letters):
    sorted_list = []
    for letter in num_letters:
        sorted_list.append({"char" : letter, "num" : num_letters[letter]})
        sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list

main()