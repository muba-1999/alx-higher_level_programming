#!/usr/bin/python3
"""Documentation for inheritance checker"""


def inherits_from(obj, a_class):
    """if the object is an instance of a class that inherited
    directly or indirectly from the specified class

    Returns:True if the object is an instance of a class
    """
    if issubclass(obj.__class__, a_class) and type(obj) != a_class:
        return True
    else:
        return False
