#!/usr/bin/python3
"""
Prints a text with 2 new lines after each of these characters: ".?:".

Functions:
    text_indentation(text)

Raises:
    TypeError: An error occurred accessing the variable type.
"""


def text_indentation(text):
    """Replaces ".?:" with two lines and prints them.

    Args:
        text (str): The text to edit.

    Raises:
        TypeError: An error occurred accessing the variable type.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n").replace(
        "?", "?\n\n").replace(":", ":\n\n").split("\n")

    for line in range(len(text)):
        print("{}".format(text[line].strip()),
              end=("" if (line == (len(text) - 1)) else "\n"))
