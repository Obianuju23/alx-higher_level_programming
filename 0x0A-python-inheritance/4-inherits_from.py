#!/usr/bin/python3
"""
This function defines a class and checks the class
"""


def inherits_from(obj, a_class):
    """Check if an obj is an instance or inherited instance of a_class."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        """checks if obj is an inheritance instance of a_class"""
        return True
    else:
        return False
