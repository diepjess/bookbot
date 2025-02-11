def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_full_book_report(book_path, text)
    
    # num_characters = get_character_dict(text)
    # print(num_characters)
    # list_num_characters = get_list_character_dict(num_characters)
    # list_num_characters.sort(reverse=True, key=sort_on)
    # print(list_num_characters)


def get_book_text(path):
    """Get the text of a book from relative path

    Args:
        path (string): Path of book

    Returns:
        string: text of the book as single string
    """
    with open(path) as f:
        return f.read()


def get_num_words(text):
    """Get number words in text

    Args:
        text (string): text of book as a single string

    Returns:
        int: number of words in text
    """
    words = text.split()
    return len(words)


def get_character_dict(text):
    """Get a dictionary of the character count in text

    Args:
        text (string): text of book as a single string

    Returns:
        dict: Keys are chars (including space and symbols) and value is their count
    """
    character_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def get_list_character_dict(char_dict):
    """Get a list of dictionaries of alpha characters and their count.

    Args:
        dict (dict): A dictionary of the character count in text. Expecting the return value of get_character_dict

    Returns:
        list: A list of dictionaries. Each dictionary has keys: "char", "num" where character is an alpha character and num is its count
    """
    new_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            new_dict = {"char": key, "num": value}
            print(new_dict)
            new_list.append(new_dict) 
    return new_list


def sort_on(dict):
    """A function that takes a dictionary and returns the value of the "num" key.
    Helper for help us sort a list of dictionaries by the value in the "num  key"

    Args:
        dict (dict): a dictionary where there is a "num" key that represents the occurances of a character

    Returns:
        int: represents the occurances of a character.
    """
    return dict["num"]


def print_full_book_report(path, text):
    print(get_header_string(path))
    print(get_word_count_string(text))
    print()
    

def get_header_string(path):
    """Generates header string for book report

    Args:
        path (string): path to text for report

    Returns:
        string: neat header that contains path to text for report
    """
    header = f"--- Begin report of {path} ---"
    return header


def get_word_count_string(text):
    """Generates statement string for work count in report

    Args:
        text (string): Text of document for report

    Returns:
        string: Statement for total word count in document for report 
    """
    num_words = get_num_words(text)
    format_num_words = f"{num_words} words found in the document"
    return format_num_words


main()