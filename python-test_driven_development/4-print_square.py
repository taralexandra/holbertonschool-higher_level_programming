#!/usr/bin/python3

"""
This function should allow to print a square made of #

"""


def print_square(size):

    """
    Print a square of certain size made of #

    Args:
        size (int): the size defined to print the square with #

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
