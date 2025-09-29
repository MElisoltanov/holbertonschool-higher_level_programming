#!/usr/bin/python3
"""This module defines the CountedIterator class that tracks iteration count."""

class CountedIterator:
    """Iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated so far."""
        return self.count
