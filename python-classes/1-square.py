#!/usr/bin/python3

"""
This file show the function Square with private instance size
"""


class Square():
    "lets define a private attribute named size"
    def __init__(self, size):
        """
            lets initialize square using a private attribute
            (and argument) named size"
        """
        self.__size = size

    pass
