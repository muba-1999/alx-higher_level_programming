#!/usr/bin/python3
def element_at(my_list, idx):
    """gets an element at the given index
    args:
        my_list: give list
        idx: index of an element
    Return:
        the element at idx
    """
    while idx < len(my_list):
        if idx < 0:
            return (None)
        else:
            return (my_list[idx])
        return (None)
