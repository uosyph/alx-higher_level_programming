#!/usr/bin/python3
"""Python bytecode MagicClass"""
import math


class MagicClass:
    """MagicClass function
    Args: radius (int or float): the radius of the object
    """

    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Defines the area of a object and return the value"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Defines the circumference of a object and return the value"""
        return 2 * math.pi * self.__radius
