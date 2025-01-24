#!/usr/bin/python3

"""
    print_square: prints a square with the character #
    size: integer
    return: None
"""


def print_square(size):

    """
    print_square: prints a square with the character #
    size: integer
    print:()
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
