#!/usr/bin/python3
def max_integer(my_list=[]):
    """checks for a maximum value in a list
    args:
        my_list: list to be checked
    Return:
        the maximum value
    """
    try:
        max_int = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max_int:
                max_int = my_list[i]
        return (max_int)
    except IndexError:
        return None
