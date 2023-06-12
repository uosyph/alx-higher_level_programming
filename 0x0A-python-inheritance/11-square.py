#!/usr/bin/python3
"""Square class that inherits from Rectangle"""


class Square(__import__('9-rectangle').Rectangle):
    """Square class"""

    def __init__(self, size):
        """init the square"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area"""
        return self.__size * self.__size

    def __str__(self):
        """Returns a formatted string"""
        return f"[Square] {self.__size}/{self.__size}"
