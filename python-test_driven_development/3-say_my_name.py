#!/usr/bin/python3

"""
This module contains the function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints a name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
