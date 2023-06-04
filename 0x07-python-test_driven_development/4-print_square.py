#!/usr/bin/python3
"""
Prints square by size input.

Functions:
    print_square(size)

Raises:
    TypeError: An error occurred accessing the variable type.
    ValueError: An error occurred accessing the variable value.
"""


def print_square(size):
    """prints square '#' by size variable.

    Args:
        size (int): Input size.

    Raises:
        TypeError: An error occurred accessing the variable type.
        ValueError: An error occurred accessing the variable value.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
