#!/usr/bin/python3

"""
    Write a func that will return True
    if if the object is an instance of,
    or if the object  is an instance of
    a class that inherited from, the
    specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """The function"""
    return isinstance(obj, a_class)
