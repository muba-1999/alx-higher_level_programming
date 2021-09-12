#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element at a specific index
    args:
        my_list: given list
        idx: the index of an element
        element: to replace with
    Return:
        a new list
    """
    list_copy = my_list[:]
    if idx < 0:
        return (list_copy)
    elif idx > len(my_list) - 1:
        return (list_copy)
    else:
        list_copy[idx] = element
        return (list_copy)
