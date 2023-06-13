#!/usr/bin/python3
"""A function that returns a dictionary description"""


def class_to_json(obj):
    """Returns a dictionary description"""
    return obj.__dict__
