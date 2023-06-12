#!/usr/bin/python3
"""Square class that inherits from Rectangle"""


class Square(__import__('9-rectangle').Rectangle):
    """Square class"""

    def __init__(self, size):
        """init the square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculates area"""
        return self.__size ** 2
