#!/usr/bin/python3
"""Documentation for the to_json_string function"""


import json


def to_json_string(my_obj):
    """converts an object to json string
    Args:
        my_obj: object to be converted to json string
    Returns:
        json representation of the string
    """
    return json.dumps(my_obj)
