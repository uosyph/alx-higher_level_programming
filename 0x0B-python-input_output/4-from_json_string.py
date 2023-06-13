#!/usr/bin/python3
"""A function that returns an object represented by a JSON string"""

from json import loads


def from_json_string(my_str):
    """Return an object represented by a JSON string"""
    return loads(my_str)
