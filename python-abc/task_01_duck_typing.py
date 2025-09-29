#!/usr/bin/python3

"""
This module defines abstract Shape, Rectangle, and Circle classes,
and a duck typing function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius


def shape_info(obj):
    """Print the area and perimeter of any shape-like object (duck typing)."""
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
