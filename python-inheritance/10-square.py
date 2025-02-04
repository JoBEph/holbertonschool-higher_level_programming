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
        """return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(BaseGeometry):
    """Square from Base geometry"""

    def __init__(self, size):
        """private size and validate integer"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """define area"""
        return self.__size * self.__size
