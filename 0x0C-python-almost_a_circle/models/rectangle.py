#!/usr/bin/python3
"""
Rectangle  class inherits from Base class with attributes height and width
"""

from models.base import Base
"""importing the Base module"""


class Rectangle(Base):
    """class Rectangle from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """This will retrieve the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """The value of the width is set at this point"""
        if type(value) != int:
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
        if type(value) != int:
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
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """This will retrives the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The value of x is set at this point"""
        self.validate_integer("y", value)
        self.__y = value

     def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """This defines and returns public method area"""
        return = self.width * self.height

    def display(self):
        """Defines display public method&prints string representation"""
        a = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(a, end='')


    def __str__(self):
         """returns a format of rectanlge, id x, y and width, height"""
       return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args):
        """Defining a module that assigns an argument to the attributes"""
        count_args = len(args)
        if count_args > 0:
            self.id = args[0]
        if count_args > 1:
            self.width = args[1]
        if count_args > 2:
            self.height = args[2]
        if count_args > 3:
            self.x = args[3]
        if count_args > 4:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """Updating instance attributes using non-keyword & keyword args"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary that represents each instance attributes"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
