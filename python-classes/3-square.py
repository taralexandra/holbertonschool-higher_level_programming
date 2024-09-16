#!/usr/bin/python3

"""
In this file, we will try to add the dimension of area of the square,
using the code we made in the previous tasks of this project
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

    def area(self):
        """
            Returns
                the area of square, size * size.
        """

        return self.__size ** 2
