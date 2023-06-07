#!/usr/bin/python3
"""Divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides a matrix by variable div.

    Args:
        matrix (matrix): The matrix to divide.
        div (int): The number used to divide.

    Raises:
        TypeError: An error occurred accessing the variable type.
        ZeroDivisionError: An error occurred accessing the variable value.

    Returns:
        new_matrix: The new divided matrix.
    """

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    for rows in matrix:
        for items in rows:
            if not isinstance(items, (int, float)):
                raise TypeError(err_matrix)

    new_matrix = []
    for rows in matrix:
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        else:
            new_matrix.append([round((items / div), 2) for items in rows])
    return new_matrix
