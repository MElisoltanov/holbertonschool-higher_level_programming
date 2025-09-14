#!/usr/bin/python3
"""Module for add_integer function.

This module provides a function to add two integers.
It validates the input types and raises exceptions if needed.
"""

def add_integer(a, b=98):
    """Adds two integers or floats.

    Args:
        a: First number (int or float).
        b: Second number (int or float, default 98).

    Returns:
        The sum as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
