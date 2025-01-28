#!/usr/bin/python3

"""
this is square module
"""


class Square:
    """
    create classe named square with typeserror and valueerror
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
