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

    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        if i != 0:
            if len(matrix[i - 1]) != len(matrix[i]):
                raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][j] = round(matrix[i][j] / div, 2) 
    return new_matrix
