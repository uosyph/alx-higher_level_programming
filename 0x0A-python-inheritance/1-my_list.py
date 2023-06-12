#!/usr/bin/python3
"""A class that inherits from a list"""


class MyList(list):
    """Prints a sorted (ascending sort) list."""

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
