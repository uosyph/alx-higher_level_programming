#!/usr/bin/python3
"""Inserting a line to a file after each line containing specific string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line to a file after each line containing specific string"""

    lines = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            lines.append(line)

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
