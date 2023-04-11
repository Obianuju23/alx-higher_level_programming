#!/usr/bin/python3

"""
This program contains the print_sorted public instance method
"""

"""a subclass of a super class list"""


class MyList(list):

    def __init__(self):
        """initializing MyList object"""
        super().__init__()

    def print_sorted(self):
        """ prints an ascending sorted list"""
        print(sorted(self))
