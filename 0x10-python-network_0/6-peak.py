#!/usr/bin/python3
"""Contains a function that finds a peak in a list"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""

    list_len = len(list_of_integers)
    if list_len == 0:
        return

    middle = list_len // 2
    pivot = list_of_integers[middle]
    left = list_of_integers[middle - 1]

    if (middle == list_len - 1 or pivot >= list_of_integers[middle + 1]) and\
            (middle == 0 or pivot >= left):
        return pivot
    elif middle != list_len - 1 and list_of_integers[middle + 1] > pivot:
        return find_peak(list_of_integers[middle + 1:])

    return find_peak(list_of_integers[:middle])
