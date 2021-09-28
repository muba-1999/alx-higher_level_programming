#!/usr/bin/python3
class Square:
    """Square"""
    def __init__(self, size=0):
        """
        initialize Square size

        args:
        size (int): size of the Square

        Return:
        None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
