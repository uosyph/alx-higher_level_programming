#!/usr/bin/python3
"""Multiplying two matrices using the NumPy module.
"""
import numpy as np


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
