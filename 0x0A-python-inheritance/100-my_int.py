#!/usr/bin/python3
"""
This is a subclass Myint that inherited from parent class int
"""


class int:
    pass


class Myint(int):
    """defines a subclass Myint from a superclass int"""
    def __eq__(self, other_objects):
        """inverts the behavior of the == and != operators"""
        return int(self) != int(other_objects)

    def __ne__(self, other_objects):
        """inverts the behavior of the == and != operators"""
        return int(self) == int(other_objects)
