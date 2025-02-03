#!/usr/bin/python3

"""create empty class base geometry"""


class BaseGeometry:
    """empty class base geo"""

    def area(self):

        """area self"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):

        """check if value is int > 0"""

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Rectangle from base geometry"""

    def __init__(self, width, height):

        """init self, width, height for rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area self for rectangle class"""

        return self.width * self.height

    def __str__(self):
        """return str"""
        return (f'[Rectangle] {self.__width}/ {self.__height}')
