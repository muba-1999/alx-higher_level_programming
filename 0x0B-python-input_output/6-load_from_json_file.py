#!/usr/bin/python3
"""Documentation fot the load_from json function"""


import json


def load_from_json_file(filename):
    """takes a json string and returns an object from a file
    Args:
        filename: file to load the string
    Returns:
        an object represented by the string in a file
    """
    with open(filename) as f:
        json_obj = json.loads(j)
    return json_obj
