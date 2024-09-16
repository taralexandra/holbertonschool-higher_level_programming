#!/usr/bin/python3
"""Define a class Square that represents a square."""


class Square:
    """A class that defines a square with a private instance attribute size"""

    def __init__(self, size=0):
        """
        Initialize the square with a private attribute `size`.

        Args:
            size (int): The size of the square, must be an integer >= 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
            Allow to print the square made of sumbols #.
            But, in case size is 0, print an empty line.
        """
        if self.__size == 0:
            print("--")
        else:
            for height in range(self.__size):
                for length in range(self.__size):
                    print("#", end="")
                print()
