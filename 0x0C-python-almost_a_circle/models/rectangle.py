#!/usr/bin/python3
"""
Rectangle  class inherits from Base class with attributes height and width
"""

from models.base import Base
"""importing the Base module"""


class Rectangle(Base):
    """class Rectangle from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This will retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """The value of the width is set at this point"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This will retrieve the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """The value of the height is set at this point"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This will retrives the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The value of x is set at this point"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This will retrives the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The value of x is set at this point"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
