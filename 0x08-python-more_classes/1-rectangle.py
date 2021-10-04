#!/usr/bin/python3
"""Documentation for the rectangle class"""


class Rectangle:
    """class that creates a rectangle"""
    def __init__(self, width=0, height=0):
        """
        initializes the rectangle class
        Args:
            width: the width of a rectangle
        Return:
            nothing
        """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of an instance
        Args:
            value(int): the width
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        Args:
            value (int): height of a rectangle
        Raises:
            ValueError: if the height is less than 0
            typeError: if the height is not an integer
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
