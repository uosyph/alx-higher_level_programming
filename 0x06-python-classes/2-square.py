#!/usr/bin/python3
"""Defines square with size that must be type int and >= 0"""


class Square:
    """A class that defines a square by size"""

    def __init__(self, size=0):
        """Initializes the size
        Args:
            size (int): value of the size
        """
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
