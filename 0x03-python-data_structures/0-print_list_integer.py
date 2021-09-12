#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print a list of integers
    args:
        my_list: list passed as an argument
    Return:
        The items in the list
    """
    for i in range(1, len(my_list)):
        print("{:d}".format(my_list[i]))
