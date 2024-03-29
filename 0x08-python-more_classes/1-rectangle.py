#!/usr/bin/python3
"""
Definition of a Rectangle class
"""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """This retrieves/gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves/gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attributes"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
