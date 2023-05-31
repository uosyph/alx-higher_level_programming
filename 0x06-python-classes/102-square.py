#!/usr/bin/python3
"""Defines Area that returns the current square area,
and can answer to comparators: ==, !=, >, >=, < and <=
based on the square area"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Initializes size"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        """Check type and value and raise error accordingly"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Defines the area of a square and return the value"""
        return self.__size ** 2

    """Answer to comparators: ==, !=, >, >=, < and <=
    based on the square area"""

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
