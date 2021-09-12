#!/usr/bin/python3
def no_c(my_string):
    """remove the character lower and uppercase c from a given string
    args:
        my_string: string passed
    Return:
        a new string
    """
    char = 'cC'
    for i in char:
        my_string = my_string.replace(i, '')
    return (my_string)
