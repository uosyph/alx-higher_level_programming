#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """init the class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area and returns the value"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a formatted string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
