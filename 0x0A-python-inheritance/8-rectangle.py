#!/usr/bin/python3
"""This function defines class Rectangle, inherited from BaseGeometry"""
BaseGeometry = __import__('7-BaseGeometry').BaseGeometry
"""
imports the super class
"""


class Rectangle(BaseGeometry):
    """Defines a subclass of a superclass BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation of the rectangle with the objects"""

        """encapsulates width and height and ensure that they are private"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
