#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file

"""


def write_file(filename="", text=""):
    """writes and returns the number of character written"""

    with write(filename, "w", encoding="utf-8") as f:
        return f.write(text)
