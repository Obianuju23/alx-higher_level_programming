#!/usr/bin/pythons
"""
This module JSON returns string representation from data hierarchies
"""
import json


def from_json_string(my_obj):
    """This function returns the JSON representation of a string object."""
    return json.dumps(my_obj)
