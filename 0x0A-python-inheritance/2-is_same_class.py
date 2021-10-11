#!/usr/bin/python3
"""Documentation for the is_same_class"""


def is_same_class(obj, a_class):
    """checks if an object is an instance of a specified class

    Returns:
        True if an object is an instance False otherwise
    """
    if type(obj) == a_class:
        return True
    else:
        return False
