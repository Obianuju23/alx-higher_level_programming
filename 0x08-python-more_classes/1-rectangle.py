#!/usr/bin/python3
"""This class defines a reactangle."""


class Rectangle:
    """This is an empty class representing a Rectangle.
    A rectangle is a quadrilateral with its parallel sides
    equal to each other."""


def __init__(self, width=0, height=0):
    """initialising the objects(width and height)of the rectangles class
    Raises:
        TypeError: if width is not an integer
        ValueError: if width is less than zero
    Args:
        width(int):The width of the rectangle
        height(int):The height of the rectangle"""
    self.width = width
    self.height = height


@property
def width(self):
    """This retrieves/gets width"""
    return self.__width


@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):
    """This retrieves/gets height"""
    return self.__height


@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
