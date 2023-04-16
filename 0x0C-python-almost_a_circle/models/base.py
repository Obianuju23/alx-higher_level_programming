#!/usr/bin/python3
"""
This class represents the base of all other classes in this project
"""


import json
import csv


class Base:
    """This defines a class named Base"""

    __nb_objects = 0
    """This is a private class attribute"""

    def __init__(self, id=None):
        """initialising thepublic attribute id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
