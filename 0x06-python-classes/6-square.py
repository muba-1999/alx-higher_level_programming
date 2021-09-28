#!/usr/bin/python3
"""Documentation for a square class"""


class Square:
    """Square"""
    def __init__(self, size, position=(0, 0)):
        """
        initialize size

        Args:
            size (int): size of square
            position (int, int): postion of the square

        Return:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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
        else:
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

    @property
    def position(self):
        """
        get position of square
        Args: None
        Return: position of the square
        """
        return self.__position

    @size.setter
    def position(self, value):
        """
        sets the postion of a square
        Args:
            value (int, int): to assign to position
        Return: None
        """
        if type(value) is tuple and len(value) == 2 and type(value[0]) is int\
                and type(value[1]) is int and value[0] >= 0 and value[1] >= 0:
            self.__posittion = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        prints square using # to stdout
        Args: None
        Return: None
        """
        if self.__size == 0:
            print()
        else:
            for c in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
