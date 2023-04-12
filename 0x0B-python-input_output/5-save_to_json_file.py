#!/usr/bin/python3
"""
This module writes an object to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an object to a text file"""

    with open(filename, "w", encoding="utf-8") as f:  
        return json.dump(my_obj, f)
