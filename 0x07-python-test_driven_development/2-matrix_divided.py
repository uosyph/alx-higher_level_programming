#!/usr/bin/python3
"""
Divides all elements of a matrix.

Functions:
    matrix_divided(matrix, div)

Raises:
    TypeError: An error occurred accessing the variable type.
    ZeroDivisionError: An error occurred accessing the variable value.
"""


def matrix_divided(matrix, div):
    """Divides a matrix by variable div

    Raises:
        TypeError: An error occurred accessing the variable type.
        ZeroDivisionError: An error occurred accessing the variable value.

    Returns:
        new_matrix: The new divided matrix
    """

    # Check if matrix is a list
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    # Check if rows in matrix is list
    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # Check if length of rows are the same
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError('Each row of the matrix must have the same size')

    # Check to see if div is zero
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Check if items in matrix are floats or ints
    for rows in matrix:
        for items in rows:
            if not isinstance(items, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    # Divides elements of a matrix
    new_matrix = []
    for rows in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
        else:
            new_matrix.append([round((items / div), 2) for items in rows])
    return new_matrix
