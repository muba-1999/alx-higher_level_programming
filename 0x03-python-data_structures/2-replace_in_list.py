#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """replaces an element at a specified index
    args:
        my_list: given list
        idx: index of an element
        element: element to be replaced
    """
    while idx < len(my_list):
        if idx < 0:
            return (my_list)
        else:
            my_list[idx] = element
            return (my_list)
    return (my_list)
