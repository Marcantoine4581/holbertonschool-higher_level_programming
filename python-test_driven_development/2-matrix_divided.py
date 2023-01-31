#!/usr/bin/python3
"""function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix.
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
        
    Raises:
        TypeError: 
            if elements of lists are non-integers and non-floats.
            if each row of the matrix have not the same size.
            if "div" is not a number.
        ZeroDivisionError:
            if "div" is equal to zero.
    """
    for row in matrix:
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = matrix[:]
    return [[round(i/div,2) for i in row] for row in new_matrix]
