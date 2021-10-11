#!/usr/bin/python3
"""Documentation a class checker"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Return: True if the object is an instance False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
