#!/usr/bin/python3

"""
This program contains the print_sorted public instance method
"""

"""a subclass of a super class list"""
class MyList(list):
    
    """initializing the subclass object"""
    def __init__(self):
        super().__init__()
    
    def print_sorted(self):
    """ prints an ascending sorted list"""
        print(sorted(self))
