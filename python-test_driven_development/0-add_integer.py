#!/usr/bin/python3

"""
    add two integers module
"""


def add_integer(a, b=98):

    """
        add_integer: add two integers
        a: integer
        b: integer
        return: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
