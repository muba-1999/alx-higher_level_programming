#!/usr/bin/python3
"""Documentation for the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """saves a json string to a file
    Args:
        my_obj: object to convert to json string
        filename: file to write to
    """
    with open(filename, 'w', encoding='utf-8'0 as f:
            json_str = json.dumps(my_obj)
            f.write(json_str)
