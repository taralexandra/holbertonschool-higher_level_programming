#!/usr/bin/python3

"""
    I am making a file to build the rectangle class
    which will allow to print a rectangle at the
    end of the project.
"""


class Rectangle():

    """
        This is the class of the rectangle
    """

    def __init__(self, width=0, height=0):

        """
            Let's make a rectangle.

            Args:

                width (int)
                height (int)
        """

    self.width = width
    self.height = height

    @property
    def width(self):
        "property to give the width of the rectangle's shape"
        return self.__width

    @width.setter
    def width(self, value):
        """
        objective is to get the value of width

        Args:
             value
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        objective here is to get value of height

        Args:
            value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
