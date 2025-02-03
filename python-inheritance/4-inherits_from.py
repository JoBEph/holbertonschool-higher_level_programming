#!/usr/bin/python3

"""
contain the function inherits_from
"""


def inherits_from(obj, a_class):
    """return true or false if the object is an instance"""
    return isinstance(obj, a_class) and type(obj) is not a_class
