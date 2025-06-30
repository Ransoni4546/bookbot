from stats import get_book_text

from stats import get_num_words

from stats import get_ch_dict

def main():
    print(f"{get_num_words(get_book_text("books/frankenstein.txt"))} words found in the document")
    print(get_ch_dict(get_book_text("books/frankenstein.txt")))    

main()