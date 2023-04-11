#!/usr/bin/python3
"""
This is a module that adds attribute: add_attribute()
"""


def add_attribute(attriobj, attriname, attrivalue):
    """the function that adds a new attribute to an object if possible"""
    if hasattr(attriobj, '__dict__'):
        setattr(attriobj, attriname, attrivalue)
    else:
        raise TypeError("can't add new attribute")
