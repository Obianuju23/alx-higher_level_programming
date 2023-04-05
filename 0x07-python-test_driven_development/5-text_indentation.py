#!/usr/bin/python3
"""
Here is "5-test_indentation" module.
It supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for b in text:
        if flag == 0:
            if b == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if b == '?' or b == '.' or b == ':':
                print(b)
                print()
                flag = 0
            else:
                print(b, end="")
