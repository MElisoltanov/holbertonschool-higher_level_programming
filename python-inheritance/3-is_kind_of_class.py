#!/usr/bin/python3
"""
This module defines a function that checks if an object
is an instance of, or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or
    a subclass thereof, otherwise False.
    """
    return isinstance(obj, a_class)
