#!/usr/bin/python3
"""
This module writes a class Student with some public attributes
"""


class Student:
    """A superclass Student from which student instances comes from"""

    def __init__(self, first_name, last_name, age):
        """initializing the attribute"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that dictionary representation of a Student instance """
        return self.__dict__
