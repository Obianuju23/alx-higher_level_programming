#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, size):
        """Intialize a new square.
        Args:
            size (int): The size of the square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = ""
        string += "[Square] {:d}/{:d}".format(self.__width, self.__height)
        return string
