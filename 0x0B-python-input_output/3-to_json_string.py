#!/usr/bin/python3
"""
This module JSON returns string representation from data hierarchies
"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of a string object."""
    return json.dumps(my_obj)
