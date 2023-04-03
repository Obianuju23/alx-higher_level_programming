#!/usr/bin/python3
"""Definition of a Rectangle class."""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of a new rectangle

        Args:
            width(int): The width of the new rectangle
            height(int): The height of the new rectangle
        Raises:
            TypeError: raised if width is not an integer
            ValueError: raised if width is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This retrieves/gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width value must be an integer")
        if value < 0:
            raise ValueError("width value must be >- 0")
        self.__width = value

    @property
    def height(self):
        """This retrieves/gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self):
        """Sets the height attributes"""
        if not isinstance(value. int):
            raise TypeError("height value must be an integer")
        if value < 0:
            raise ValueError("height value must be >= 0")
        self.__width = value

    def area(self):
        """returns the attribute(area) of the  rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the attribute(perimeter) of the rectangle"""
        if self.__width or self.__height == 0:
            return(0)
            return ((self.__width * 2) + (self.__height * 2))
