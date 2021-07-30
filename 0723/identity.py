"""
Identity Matrix

An identity matrix is defined as a square matrix with 1s running from the top left of the square to the
bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the
general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this
challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions..
It does not matter if the mirror image is left-right or top-bottom.
Examples
id_mtrx(2) ➞ [
[1, 0],
[0, 1]
]
id_mtrx(-2) ➞ [
[0, 1],
[1, 0]
]
id_mtrx(0) ➞ []
"""


def _normal(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def _inverse(n):
    return [[1 if i == n - (j + 1) else 0 for j in range(n)] for i in range(n)]


def identity(n):
    return _normal(n) if n >= 0 else _inverse(-n)


if __name__ == '__main__':

    from sys import argv
    from pprint import pprint
    pprint(identity(int(argv[1])))
