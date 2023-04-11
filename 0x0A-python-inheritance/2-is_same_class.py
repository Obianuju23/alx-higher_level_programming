#!/usr/bin/python3

def is_same_class(obj, a_class):
    """This protype returns True if the object given is an instance of the
    specified class.
    """

    """checking if object is exactly same as the specified class"""
 
    if type(obj) == a_class:
         return True
    else:
         return False
