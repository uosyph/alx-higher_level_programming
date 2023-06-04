#!/usr/bin/python3
import numpy as np
"""
Multiplying two matrices using the NumPy module.

Functions:
    lazy_matrix_mul(m_a, m_b)

Raises:
    Exception: An error occurred.
"""


def lazy_matrix_mul(m_a, m_b):
    """Multiples two matrices.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        new_matrix: The new product matrix.

    Raises:
        Exception: An error occurred.
    """

    try:
        return np.matmul(m_a, m_b)
    except:
        raise
