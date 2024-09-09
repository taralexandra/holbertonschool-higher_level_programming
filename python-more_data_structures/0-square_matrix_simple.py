#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    the_squared_matrix = []

    for row in matrix:
        the_squared_row = []
        for element in row:
            the_squared_row.append(element ** 2)
        the_squared_matrix.append(the_squared_row)

    return the_squared_matrix
