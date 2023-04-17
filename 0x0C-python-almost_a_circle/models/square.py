#!/usr/bin/python3
"""
Square class inherits from Rectangle class with some attributes
"""

from models.rectangle import Rectangle
"""importing the Rectangle module"""


class Square(Rectangle):
    """class Square from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a format of square, id x, y and width, height"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """This will retrieve the size of the Rectangle"""
        return self.__width

    @size.setter
    def size(self, value):
        """The value of the size(width&height) is set at this point"""
        self.width = value
        self.height = value

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
        """Returns dictionary representation of a Rectangle attributes"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
