#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Class that defines a Square by its size."""
    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
