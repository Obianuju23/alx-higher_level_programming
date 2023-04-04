#!/usr/bin/python3
"""Definition of a Rectangle class."""


class Rectangle:
    """This represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of a new rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the attribute(area) of the  rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the attribute(perimeter) of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """This returns informal printable Rectangle representation
        with # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        Rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    Rectangle += str(self.print_symbol)
                except Exception:
                    Rectangle += type(self).print_symbol
            if column < self.__height - 1:
                Rectangle += "\n"
        return (Rectangle)

    def __repr__(self):
        """returns rectangle string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message whenever rectangle instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the rectangles with the biggest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new rectangle with the height and weight equal to size"""
        return Rectangle(size, size)
