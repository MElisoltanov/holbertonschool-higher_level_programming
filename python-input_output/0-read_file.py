#!/usr/bin/python3
"""Reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Reads a texte file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(, end=""))
