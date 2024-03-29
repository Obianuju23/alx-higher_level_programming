#!/usr/bin/python3
"""
This module is a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """appends and returns the number of characters added"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
