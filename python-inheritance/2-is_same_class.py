#!/usr/bin/python3

"""
this module permit to know if an object is an instance of a class
"""


def is_same_class(obj, a_class):

    """return true or false if the object is an instance of the class"""
    return type(obj) is a_class
