#!/usr/bin/python3
"""Documentation for the from_json_string(my_str) function"""


import json


def from_json_string(my_str):
    """converts a json string to an object
    Args:
        my_str: string to be converted to an object
    Returns:
        an object representation of a json string
    """
    return json.loads(my_string)
