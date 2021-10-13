#!/usr/bin/python3
"""Documentation for the write_file function"""


def write_file(filename="", text=""):
    """writes text to a given file

    Args:
        filename: the file to be written to
        text: text to write to a file

    Returns: number of characters written
    """
    count = 0
    with open(filename, 'w', encoding='utf8') as f:
        w_file = f.write(text)
    return w_file
