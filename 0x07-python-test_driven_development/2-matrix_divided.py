#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not all(isinstance(row, list) 
    and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    return new_matrix
