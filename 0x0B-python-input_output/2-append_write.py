#!/usr/bin/python3
"""Documentation for append_write function"""


def append_write(filename="", text=""):
    """apeends text to a file
    Args:
        filename: file to append to
        text: text to append to a given file
    Returns:
        number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        w_file = f.write(text)
    return w_file
