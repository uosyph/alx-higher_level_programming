#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializes public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation"""
        return self.__dict__
