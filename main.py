def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def book_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def main():
    print(f"{book_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()