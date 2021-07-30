"""
describe a way to shift the zeroes in a list
to its tail
"""


def golberg_zero_machine(vec):
    string = ''.join(map(str, vec))
    return list(map(int, string.replace('0', '') + '0' * string.count('0')))


if __name__ == '__main__':

    v = [1, 2, 0, 3, 0, 4, 0, 5]
    print(golberg_zero_machine(v))
