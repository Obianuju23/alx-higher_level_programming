#!/usr/bin/python3
"""
this module adds and saves all arguments to a python list
"""
import sys
"""imports the module needed to get arguments"""

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    """imports the function save_to_json_file from task 5"""

    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    """imports the function load_from_json_file from task 6"""

    try:
        item_content = load_from_json_file("add_item.json")
    except Exception:
        item_content = []
    item_content.extend(sys.argv[1:])
save_to_json_file(item_content, "add_item.json")
