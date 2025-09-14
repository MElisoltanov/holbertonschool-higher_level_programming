#!/usr/bin/python3
"""Module for print_square function.

This module provides a function to print a square of # characters.
"""

def print_square(size):
    """Prints a square with the character #.

    Args:
        size: size length of the square (int).

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
