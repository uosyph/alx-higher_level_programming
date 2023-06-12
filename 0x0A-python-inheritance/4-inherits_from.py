#!/usr/bin/python3
"""Checks if object is inherits from a class."""


def inherits_from(obj, a_class):
    """Checks if object is inherits from a class."""

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
