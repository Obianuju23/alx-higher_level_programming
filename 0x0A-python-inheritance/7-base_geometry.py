#!/usr/bin/python3
"""
This function defines an empty class
"""


class BaseGeometry:
    """An empty class BaseGeometry"""
    def area(self):
        """raises exception once area is not implementated"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value & ensure it is integer greater than 0"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
