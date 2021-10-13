#!/usr/bin/python3
"""Documentation for read_file function"""


def read_file(filename=""):
    """reads data in a given file

    Args:
        filename: the file to read
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
