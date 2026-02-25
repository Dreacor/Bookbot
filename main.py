def get_book_text(filepath):

    #filepath = "/home/dreacor/coding/bootdotdev/bookbot/books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()

def main():
    get_book_text("./books/frankenstein.txt")

main()