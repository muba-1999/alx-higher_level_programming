#!/usr/bin/python3
"""Documentation for a square class"""

class Square:
    """Square"""
    def __init__(self, size=0):
        """
        initialize Square size

        Args:
            size (int): size of the Square
        Raises:
            TypeError: When the value passed in is not an integer
            ValueError: When the value passed in is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
