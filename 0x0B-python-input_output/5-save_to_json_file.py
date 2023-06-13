#!/usr/bin/python3
"""A function that writes an Object to text file"""

from json import dump


def save_to_json_file(my_obj, filename):
    """Writes an Object to text file using JSON representation"""

    with open(filename, "w", encoding="UTF-8") as f:
        dump(my_obj, f)
