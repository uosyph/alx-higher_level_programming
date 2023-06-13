#!/usr/bin/python3
"""A function that writes to a file"""


def write_file(filename="", text=""):
    """Writes a string to a file and returns the number of chars written"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
