def get_num_words(text):
    """Get number words in text

    Args:
        text (string): text of book as a single string

    Returns:
        int: number of words in text
    """
    words = text.split()
    return len(words)