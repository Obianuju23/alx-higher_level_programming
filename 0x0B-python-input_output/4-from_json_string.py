#!/usr/bin/python3
"""
This module returns object (Python data structure)
from JSON string representation
"""
import json


def from_json_string(my_str):
    """This function deserialises(i.e returning data from a string)string"""
    return json.loads(my_str)
