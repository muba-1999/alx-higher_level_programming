#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Square"""
    def __init__(self, size):
        """
        initialize size

        Args:
            size (int): size of square

        Return:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size

        Args:
            value: valur to assign to size
        Return:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculates the area of a square

        Args:
            None
        Return:
            area of a square
        """
        return self.__size ** 2
