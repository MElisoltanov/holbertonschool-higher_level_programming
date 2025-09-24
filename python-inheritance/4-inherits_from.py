#!/usr/bin/python3
"""
This module provides a function to determine if an object is an instance
of a subclass of a specified class, but not an instance of the class itself.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of
    a subclass of a_class (not a_class itself).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
