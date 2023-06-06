#!/usr/bin/python3
"""Prints the first and last name.
"""


def say_my_name(first_name, last_name=""):
    """Joins two strings and prints them.

    Args:
        first_name (str): First name.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: An error occurred accessing the variable type.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
