#!/usr/bin/python3
"""Module that validates an integer."""


class BaseGeometry:
    """Basic class definition"""

    def area(self):
        """Empty method only used to raise an exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")