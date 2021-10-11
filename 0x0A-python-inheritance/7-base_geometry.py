#!/usr/bin/python3
"""Documentation for BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator
        Args:
            name (str): name of the string
            value (int): value to validate
        Returns:
            TypeError if value is not an integer
            ValueError if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
