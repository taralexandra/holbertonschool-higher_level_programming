#!/usr/bin/python3

"""
This file is the function that allow to divide a matrix with an integer

"""


def matrix_divided(matrix, div):

	"""
    Divide a matrix with an integer.

    Args:
        matrix (list): matrix we want to divide.
        div (int, float): the number we want to use to divide.

     """

     if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
