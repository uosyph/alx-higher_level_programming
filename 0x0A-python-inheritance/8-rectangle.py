#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""


class Rectangle(__import__('7-base_geometry').BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """init the class"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
