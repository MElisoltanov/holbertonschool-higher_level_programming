#!/usr/bin/python3
"""Defines a student class with atribute filering."""


class Student:
    """Defines a student by first_name, last_name and age."""


    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance."""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
