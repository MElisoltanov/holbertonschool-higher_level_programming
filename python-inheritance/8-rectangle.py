#!/usr/bin/python3
"""This module defines the Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Both width and height are validated as positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
