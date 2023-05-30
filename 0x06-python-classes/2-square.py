#!/usr/bin/python3
"""Defines square with size that must be type int and >= 0"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes Square with size"""
        self.__size = size
        """Checks type and value and raise error accordingly"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
