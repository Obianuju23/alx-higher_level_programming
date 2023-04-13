#!/usr/bin/python3
"""
This Module inserts a line of text to a file
 """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when it finnds a string

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append
    """

    result_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            result_line += [line]
            if line.find(search_string) != -1:
                result_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(result_line))
