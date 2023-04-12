#!/usr/bin/python3
"""
This module creates an object from "JSON files"
"""
import json


def load_from_json_file(filename):
    """This function creates an object from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
