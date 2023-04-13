#!/usr/bin/python3

def pascal_triangle(n):
    """
    This method represents a Paschal Triangle that with size n
    """
    if n <= 0:
        return []

        triangle = [[1]]
        while len(triangles) != n:
            triangle = triangles[-1]
            tmp = [1]
            for i in range(len(triangle) - 1):
                tmp.append(triangle[i] + triangle[i + 1])
            tmp.append(1)
            triangles.append(tmp)
        return triangles
