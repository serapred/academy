"""
Write a program that identifies numbers inside
a txt file and computes:
    - digit occurrence
    - lowest recurring numbers
    - highest recurring numbers
"""


def find_digits(file):
    cnt = [0] * 10
    with open(file, 'r') as f:
        for line in f:
            for char in line:
                if char.isdigit():
                    cnt[int(char)] += 1
    return cnt


def minmax_digits(digits):
    minval, maxval = min(digits), max(digits)
    mindex, maxdex = [], []

    for i, q in enumerate(digits):
        if q == minval:
            mindex.append(i)
        if q == maxval:
            maxdex.append(i)

    return {'value': minval, 'index': mindex}, {'value': maxval, 'index': maxdex}


def count_digits(file):

    d = find_digits(file)
    mind, maxd = minmax_digits(d)
    return {'digits': d, 'min': mind, 'max': maxd}


if __name__ == '__main__':

    path = '../files/'

    import pprint as pp
    cnt = count_digits(path + 'numbers.txt')
    pp.pprint(cnt)
