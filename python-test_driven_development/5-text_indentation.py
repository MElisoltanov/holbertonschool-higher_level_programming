#!/usr/bin/python3
"""Module for text_indentation function.

This module provides a function to print a text with 2 new lines after each '.', '?' and ':'.
"""

def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':'.

    Args:
        text: The text to print (str).

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    while i < n:
        # Skip leading spaces
        while i < n and text[i] == ' ':
            i += 1
        if i >= n:
            break
        if text[i] in ".:?":
            print(text[i], end="\n\n")
            i += 1
            # Skip spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")
            i += 1
