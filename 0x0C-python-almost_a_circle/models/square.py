#!/usr/bin/python3
"""
Square class inherits from Rectangle class with some attributes
"""

from models.rectangle import Rectangle
"""importing the Rectangle module"""


class Square(Rectangle):
    """class Square(subclass)from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a format of square, id x, y and width, height"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """This will retrieve the size of the Rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """The value of the size(width&height) is set at this point"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """Internal method that updates instance attributes with */**args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updating instance attributes using non-keyword & keyword args"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle attributes"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
