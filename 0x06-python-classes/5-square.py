#!/usr/bin/python3
class Square:
    """Square"""
    def __init__(self, size=0):
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
            value (int): value to be assigned to size
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

    def my_print(self):
        """
        prints a square with #
        Args:
            None
        Return:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
