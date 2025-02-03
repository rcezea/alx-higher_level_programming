#!/usr/bin/python3
"""Divide all elements of a matrix."""


def matrix_divided(matrix, div=1):
    """Divide all elements of a matrix."""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    length = len(matrix[0])

    new_matrix = []

    for i in range(len(matrix)):

        if len(matrix[i]) != length:
            raise TypeError('Each row of the matrix must have the same size')

        if not isinstance(matrix[i], list):
            raise TypeError(
                f'matrix must be a matrix '
                f'(list of lists) of integers/floats')

        new_matrix.append([])

        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError(
                    f'matrix must be a matrix '
                    f'(list of lists) of integers/floats')

            new_matrix[i].append(round(matrix[i][j] / div, 2))

    return new_matrix
