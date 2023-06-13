#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file"""

    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
