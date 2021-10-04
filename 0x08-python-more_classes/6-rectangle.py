#!/usr/bin/python3
"""Documentation on the rectangle class"""


class Rectangle:
    """class to create a rectangle"""
    def __init__(self, width=0, height=0):
        """
        initializes the rectangle class
        Args:
            width (int): the width of a rectangle
            height )int): the height of a rectangle
        Return:nothing
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
        sets the width of a rectangle
        Args:
            value (int): the width of a rectangle
        Raises:
            ValueError: when width is 0
            TypeError: when width is not int
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
        sets the height of the rectangle
        Args:
            value (int): height of a rectangle
        Raises:
            ValueError: when height is 0
            TypeError: when height is not an integer
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i is not self.__height - 1:
                rectangle.append('\n')
        return ''.join(rectangle)

    def __repr__(self):
        string = []
        string.append('Rectangle(')
        string.append(str(self.__width) + ',' + str(self.__height) + ')')
        return ''.join(string)

    def __del__(self):
        print('Bye rectangle...')
