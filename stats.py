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
            new_list.append(new_dict) 
    return new_list


def get_sorted_list_character_dict(text):
    """Get a sorted list of dictionarys of alpha characters by their occurance

    Args:
        text (string): text of document

    Returns:
        list: sorted list of dictionaries by their occurance
    """
    char_dict = get_character_dict(text)
    list_num_char = get_list_character_dict(char_dict)
    list_num_char.sort(reverse=True, key=sort_on)
    return list_num_char


def sort_on(dict):
    """A function that takes a dictionary and returns the value of the "num" key.
    Helper for help us sort a list of dictionaries by the value in the "num  key"

    Args:
        dict (dict): a dictionary where there is a "num" key that represents the occurances of a character

    Returns:
        int: represents the occurances of a character.
    """
    return dict["num"]