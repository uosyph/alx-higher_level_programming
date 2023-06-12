#!/usr/bin/python3
"""A class that inherits from a list"""


class MyList(list):
    """Public instance method that prints a list,
    but sorted (ascending sort)."""

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
