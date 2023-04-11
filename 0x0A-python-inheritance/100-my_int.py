#!/usr/bin/python3
"""
This is a subclass Myint that inherited from parent class int
"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, other):
        """Override == opeartor with != behavior."""
        return self.real != other

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return self.real == other
