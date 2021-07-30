"""
Write a program that requires the user to input numbers. '0' is the exit state.
if the inserted number is multiple of 2 print "flip", if it is a multiple of 3 print
"flop" instead. (what happens when a number is multiple of 6?)
"""


def fizzBuzz(n=-1):

    while n != 0:
        try:
            n = float(input('insert number: '))
        except ValueError:
            print('Not a Number')
            return -1
        print(inner(n))

    return n


def inner(n=-1):

    res = ''
    if n == 0:
        return ''
    if n % 2 == 0:
        res += 'flip'
    if n % 3 == 0:
        res += 'flop'

    return res


if __name__ == '__main__':

    fizzBuzz()
