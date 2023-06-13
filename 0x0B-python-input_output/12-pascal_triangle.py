#!/usr/bin/python3
"""The Pascal's Triangle"""


def pascal_triangle(n):
    """Returns a list of lists of ints representing Pascal's triangle of n"""

    list_of_lists = []
    if n > 0:
        list_of_lists.append([1])
        for i in range(1, n):
            prev = list_of_lists[-1]
            list_of_lists.append([1] + [prev[j - 1] + prev[j]
                                 for j in range(1, i)] + [1])
    return list_of_lists
