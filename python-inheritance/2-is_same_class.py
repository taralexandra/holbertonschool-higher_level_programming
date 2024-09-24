#!/usr/bin/python3

"""
    Func that will return True if the object
    is exactly an instance of the specified class
    or False otherwise
"""


def is_same_class(obj, a_class):
    """
     object is exactly an instance of
    the specified class
    """
    return type(obj) is a_class
