#!/usr/bin/python3
"""
This module defines a function that reads a text file
"""


def read_file(filename=""):
    """Reads and prints the UTF8 text file content to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(f.read(), end="")
