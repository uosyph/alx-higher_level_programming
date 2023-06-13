#!/usr/bin/python3
"""A function that creates an Object from a JSON file"""

from json import load


def load_from_json_file(filename):
    """Creates an Object from a JSON file"""

    with open(filename, encoding="UTF-8") as f:
        return load(f)
