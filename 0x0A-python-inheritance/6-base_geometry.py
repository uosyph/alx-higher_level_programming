#!/usr/bin/python3
"""Module that raises an exception message"""


class BaseGeometry:
    """Basic class definition"""

    def area(self):
        """Empty method only used to raise an exception message"""
        raise Exception("area() is not implemented")
