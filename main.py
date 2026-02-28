
from stats import get_word_count, get_character_count, get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_word_count(text)

    num_characters = get_character_count(text)

    sorted_chars = get_sorted_list(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")


main()