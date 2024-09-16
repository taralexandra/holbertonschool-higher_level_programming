#!/usr/bin/python3

"""
In this file we will chez size is an integer, otherwise raise a typeerror
and if size is negative, less thn 0, raise value error, each must have a
specific message
"""


class Square:
    "lets define a private attribute named size"
    def __init__(self, size=0):
        """
            lets initialize square using a private attribute
            (and argument) named size

            Args:

                size (int): the size of the square, initialize at 0,
                must be an integer and >= 0 (superieur a 0).

            Raises:

                TypeError: if size is not an integer.
                ValueError: if value of size  is < 0.
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
