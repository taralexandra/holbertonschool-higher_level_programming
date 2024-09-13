#!/usr/bin/python3
"""
   This file is the 0-the add_integer module.

   This module contains the add_integer function.

"""


def add_integer(a, b=98):

    """
    Add 2 ints

    Args:
        a (int): integer a
        b (int): integer b

    Raises:
        TypeError exception if a or b are not integers or floats

    Returns:
        The result of the add between a + b.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
