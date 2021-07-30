""" demonstrate zip/map usage in a practical example """

# matrix rotation


def rotate(matrix):
    return list(map(list, list(zip(*matrix[:]))))

# matrix to string


def strmat(matrix):
    res = ''
    for i in matrix:
        res += '\t'.join(map(str, i)) + '\n'
    return res

# same but one line


def strmat(matrix):
    return '\n'.join(map(str, ('\t'.join(map(str, x)) for x in matrix)))


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(strmat(rotate(matrix)))
