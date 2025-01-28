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
        self.position = (0, 0)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("check every element of position")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("check either element if less than 0")
        self.__position = value

    def area(self):
        """
        calculate area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print square
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
