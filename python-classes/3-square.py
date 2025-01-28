#!/usr/bin/python3

"""
this is square module
"""


class Square:
    """
    typeserror and valueerror and define the area
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
