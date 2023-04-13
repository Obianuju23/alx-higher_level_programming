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

    def to_json(self, attrs=None):
        """function that retrieves dictionary representation of Student"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
            """a here is attribute"""
        return self.__dict__

    def reload_from_json(self, json):
        """this method  replaces all attributes of the Student instance:"""
        for key, value in json.items():
            setattr(self, key, value)
