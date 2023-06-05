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
        Draw a rectangle: rectangle with the character #.
        Rectangle: The width and height.

    Raises:
        TypeError: An error occurred accessing the variable type.
        ValueError: An error occurred accessing the variable value.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        for _ in range(self.__height):
            for _ in range(self.height - 1):
                print(str(self.print_symbol) * self.__width)
            return str(self.print_symbol) * self.width

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
