#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initializes public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation"""
        if not isinstance(attrs, list) or attrs is None:
            return self.__dict__

        dict_rep = {}
        for attr in attrs:
            if not isinstance(attr, str):
                return self.__dict__
            if attr in self.__dict__.keys():
                dict_rep[attr] = self.__dict__[attr]
        return dict_rep

    def reload_from_json(self, json):
        """Replaces all the attributes of the instances"""
        for attr in json.keys():
            self.__dict__[attr] = json[attr]
