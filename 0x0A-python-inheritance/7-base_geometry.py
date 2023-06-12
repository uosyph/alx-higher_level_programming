#!/usr/bin/python3
"""Module that validates an integer."""


class BaseGeometry:
    """Basic class definition"""

    def area(self):
        """Empty function only used to raise an exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates the value"""
        if not isinstance(value, int) or not issubclass(int, type(value)):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
