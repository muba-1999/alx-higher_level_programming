#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints a list in reverse
    args:
        my_list: given list
    Return:
        element of the list in reverse
    """
    for i in my_list[::-1]:
        print("{:d}".format(i))
