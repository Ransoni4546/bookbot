def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(full_book):
    num_words = len(full_book.split())
    return num_words

def get_ch_dict(book):
    lower_case_book = book.lower()
    ch_dict = {}
    for ch in lower_case_book:
        ch_dict[ch] = ch_dict.get(ch, 0) + 1
    return ch_dict
    