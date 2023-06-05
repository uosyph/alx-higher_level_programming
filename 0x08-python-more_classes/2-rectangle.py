#!/usr/bin/python3
"""
A class that defines a rectangle.
"""


class Rectangle:
    """Define a Rectangle type

    Returns:
        Width: The width of the rectangle.
        Height: The height of the rectangle.
        Area: The rectangle area.
        Perimeter: The rectangle perimeter.

    Raises:
        TypeError: An error occurred accessing the variable type.
        ValueError: An error occurred accessing the variable value.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 0 if self.width == 0 or self.height == 0 else 2 * (self.height + self.width)
