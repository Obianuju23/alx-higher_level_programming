#!/usr/bin/python3
"""
this module adds and saves all arguments to a python list
"""

from sys import argv
"""imports the module needed to get arguments"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""imports the function save_to_json_file from task 5"""
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
"""imports the function load_from_json_file from task 6"""

filename = "add_item.json"

try:
    obj = load_from_json_file(filename)
except FileNotFoundError:
    obj = []

save_to_json_file(obj + argv[1:], filename)
