#!/usr/bin/python3
"""
This function defines a class and checks the class
"""


def is_kind_of_class(obj, a_class):
 """Check if an object is an instance or inherited instance of a class."""

    if isinstance (obj, a_class):
    """checks if obj is an instance of a_class"""
        return True
    else:
        return False
