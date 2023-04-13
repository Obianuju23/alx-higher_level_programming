#!/usr/bin/python3
"""
This Module returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """This Function retuns the dictionary description of an object """

    item = {}
    if hasattr(obj, "__dict__"):
        item = obj.__dict__.copy()
    return item
