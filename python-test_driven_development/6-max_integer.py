#!/usr/bin/python3
"""Module for max_integer function."""

def max_integer(list=[]):
    """Finds and returns the max integer in a list of integers.

    Args:
        list: list of integers (default empty).

    Returns:
        The largest integer in the list, or None if the list is empty.
    """
    if len(list) == 0:
        return None
    max_val = list[0]
    for i in list:
        if i > max_val:
            max_val = i
    return max_val
