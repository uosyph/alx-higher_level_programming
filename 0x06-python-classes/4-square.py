#!/usr/bin/python3
"""Defines Area that returns the current square area"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initializes size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        """Check type and value and raise error accordingly"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    """Defines the area of a square
    Return: area of square"""

    def area(self):
        return self.__size ** 2
