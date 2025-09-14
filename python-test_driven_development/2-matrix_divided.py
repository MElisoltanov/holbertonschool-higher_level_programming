#!/usr/bin/python3
"""Module for matrix_divided function.

This module provides a function to divide all elements of a matrix by a number.
It validates the input types and raises exceptions if needed.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix: list of lists of integers or floats.
        div: number (int or float) to divide by.

    Returns:
        New matrix with divided values.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]