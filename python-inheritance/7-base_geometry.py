#!/usr/bin/python3

"""create empty class base geometry"""


class BaseGeometry:
    """empty class base geo"""

    def area(self):

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):

        """check if value is int > 0"""

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
