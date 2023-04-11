#!/usr/bin/python3
"""
 The module `8-rectangle'has two classes;superclass
BaseGeometry() and Rectangle which is a sub
class of BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
imports the super class
"""


class Rectangle(BaseGeometry):
    """defines a class Rectangle which is a subclass of BaseGeometry"""
    def __init__(self, width, height):
        """initializes and  validates width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
