#!/usr/bin/python3
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
        self.__size = value

    def area(self):
        """
        calculates the area of a square

        Args:
            None
        Return:
            area of a square
        """
    def __str__(self):
        """
        prints a square to the stdout using #
        Args:None
        Return: None
        """
        new = ""
        if self.__size == 0:
            return new
        else:
            for k in range(self.__position[1]):
                new += "\n"
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    new += " "
                for c in range(self.__size):
                    new += "#"
                if i == self.__size -1:
                    new += ""
                else:
                    new += "\n"
        return new
