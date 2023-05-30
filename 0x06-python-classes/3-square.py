#!/usr/bin/python3
"""Defines Area that returns the current square area"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes Square with size"""
        self.__size = size
        """Check type and value and raise error accordingly"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    """Defines the area of a square
    Return: area of square"""

    def area(self):
        return self.__size ** 2
