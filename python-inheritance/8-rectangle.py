#!/usr/bin/python3

"""create empty class base geometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle from base geometry"""

    def __init__(self, width, height):
        """init self, width, height for rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
