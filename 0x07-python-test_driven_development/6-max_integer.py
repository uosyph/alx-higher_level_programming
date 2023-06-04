#!/usr/bin/python3
"""
Find the max integer in a list.

Functions:
    max_integer(list=[])
"""


def max_integer(list=[]):
    """Find the max integer in a list of integers

    Args:
        list (list of ints): The list to check, Defaults to empty list.

    Returns:
        None: If the list is empty.
        result: The max integer.
    """

    if len(list) == 0:
        return

    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
