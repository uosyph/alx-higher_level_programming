#!/usr/bin/python3
"""
Adds two integers.

Functions:
    0-add_integer(a,b=98)

Raises:
    TypeError: An error occurred accessing the variable type.
"""


def add_integer(a, b=98):
    """Sums two integers, and checks if a/b is int or float type.

    Args:
        a (int): First number.
        b (int, optional): Second number, Defaults to 98.

    Raises:
        TypeError: An error occurred accessing the variable type.

    Returns:
        a + b: The sum of the two integers
    """

    if type(a) is int or type(a) is float:
        if type(b) is int or type(b) is float:
            return int(a) + int(b)
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
