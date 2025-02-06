#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""create empty class base geometry"""


class Rectangle(BaseGeometry):
    """Rectangle from base geometry"""

    def __init__(self, width, height):
        """init self, width, height for rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
