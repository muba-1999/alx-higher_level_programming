#!/usr/bin/python3
"""Documentation for the Mylist class"""


class MyList(list):
    """MyList class that inherits from the List class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
