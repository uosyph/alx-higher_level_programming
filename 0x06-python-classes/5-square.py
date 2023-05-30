#!/usr/bin/python3
"""Prints to stdout the square with the character #"""


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

    def area(self):
        """Defines the area of a square and return the value"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with character #"""
        for _ in range(self.__size):
            for _ in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
