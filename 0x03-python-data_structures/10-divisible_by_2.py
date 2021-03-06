#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Checks if a nuber in the list is divisible by 2
    args:
        my_list: list given
    Return:
        new list of true or false
    """
    if not my_list:
        return (my_list)
    new_list = list(my_list)
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    return (new_list)
