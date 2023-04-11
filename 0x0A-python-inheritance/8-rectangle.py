#!/usr/bin/python3
"""
This function defines an empty class
"""


class BaseGeometry:
    """An empty class BaseGeometry"""


class Rectangle(BaseGeometry):
    """Defines a subclass of a superclass BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation of the rectangle with the objects"""
        self.integer_validator("width", width)
        """encapsulates width and make it private"""
        self.__width = width
        self.integer_validator("height", height)
        """encapsulates width and make it private"""
        self.__height = height
