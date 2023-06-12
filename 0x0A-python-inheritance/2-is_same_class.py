#!/usr/bin/python3
"""Module contains a function that returns Trueif the object is
exactly an instance of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """Checks if the object is exactly an instance of the specified class."""

    return type(obj) is a_class
