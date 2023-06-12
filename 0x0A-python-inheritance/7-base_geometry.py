#!/usr/bin/python3
"""Module that validates an integer."""


class BaseGeometry:
    """Basic class definition"""

    def area(self):
        """Empty method only used to raise an exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value"""
        if not issubclass(int, type(value)) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
