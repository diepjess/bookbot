def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words in the file")
    num_characters = get_character_dict(text)
    # print(num_characters)
    print(get_list_character_dict(num_characters))


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


main()