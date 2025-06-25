from stats import (
    get_num_words, 
    get_sorted_list_character_dict,
)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print_full_book_report(book_path, text)


def get_book_text(path):
    """Get the text of a book from relative path

    Args:
        path (string): Path of book

    Returns:
        string: text of the book as single string
    """
    with open(path) as f:
        return f.read()


def print_full_book_report(path, text):
    """Print book report with header, footer, word count, and alpha character occurances

    Args:
        path (string): path to document
        text (string): text of document
    """
    print(get_header_string())
    print(get_analyze_string(path))
    print(get_sub_header_word_count())
    print(get_word_count_string(text))
    print(get_sub_header_char_count())
    print_char_occurance(text)
    print(get_footer_string())
    

def get_header_string():
    """Generates header string for book report

    Args:
        path (string): path to text for report

    Returns:
        string: neat header that contains path to text for report
    """
    header = f"============ BOOKBOT ============"
    return header


def get_analyze_string(path):
    analyze = f"Analyzing book found at {path}..."
    return analyze
    

def get_sub_header_word_count():
    sub_header = f"----------- Word Count ----------"
    return sub_header


def get_sub_header_char_count():
    sub_header = f"--------- Character Count -------"
    return sub_header

def get_word_count_string(text):
    """Generates statement string for work count in report

    Args:
        text (string): Text of document for report

    Returns:
        string: Statement for total word count in document for report 
    """
    num_words = get_num_words(text)
    format_num_words = f"Found {num_words} total words"
    return format_num_words


def get_footer_string():
    """Generates footer stirng for book report

    Returns:
        string: Neat final statement marking end of report
    """
    footer = "============= END ==============="
    return footer


def print_char_occurance(text):
    """Prints character and occurance sorted by occurance of text

    Args:
        text (string): text of document
    """
    char_occurance = get_sorted_list_character_dict(text)
    for item in char_occurance:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")


main()