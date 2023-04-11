#!/usr/bin/python3
"""
This is a subclass Myint that inherited from parent class int
"""


class Myint(int):
    """defines a subclass Myint from a superclass int"""

    def __eq__(self, value):
        """inverts the behavior of the == and != operators"""
        return int(self) != value

    def __ne__(self, value):
        """inverts the behavior of the == and != operators"""
        return int(self) == value
