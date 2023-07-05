#!/usr/bin/python3
import numpy as np
""" matrix multiplication function using NumPy."""

def lazy_matrix_mul(m_a, m_b):
    """ multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): first matrix.
        m_b (list of lists of ints/floats): second matrix.
    """

    return (np.matmul(m_a, m_b))
