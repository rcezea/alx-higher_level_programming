#!/usr/bin/python3
def matrix_divided(matrix, div):
    valuetype = (int, float)
    if not isinstance(div, valuetype):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    oldLength = len(matrix[0])
    new_matrix = []
    for i in matrix:
        new_row = []
        if oldLength != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, valuetype):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(j/div, 2))
        new_matrix.append(new_row)
    return new_matrix
