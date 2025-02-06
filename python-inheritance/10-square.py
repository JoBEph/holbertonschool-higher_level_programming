#!/usr/bin/python3

"""create empty class base geometry"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """lalalala"""

    def __init__(self, size):
        """private size and validate integer"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """define area"""
        return self.__size * self.__size
