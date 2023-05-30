#!/usr/bin/python3
class Square:
    __size = 0

    def __init__(self, size=None):
        if size is not None:
            self.__dict__ = {'_Square__size': size}
