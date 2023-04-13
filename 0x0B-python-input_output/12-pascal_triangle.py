#!/usr/bin/python3

def pascal_triangle(n):
    """
    This method represents a Paschal Triangle that with size n
    """
    if n <= 0:
        return []

    elif n == 1:
        return [[1]]

    else:
        triangle = [[1]]
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
    return triangle 
