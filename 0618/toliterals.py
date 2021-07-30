"""
Given an input string of digits, convert it into
its literal representation.
Ex:
to_literals('123') 'one two three'
"""

NUMMAP = {
    '-': 'minus', '+': 'plus',
    '0': 'zero', '1': 'one',
    '2': 'two', '3': 'three',
    '4': 'four', '5': 'five',
    '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine',
}


def to_literals(number):
    return ' '.join(tuple(NUMMAP[i] for i in number))


def is_str_int(string):
    """helper function, 1 to account sign"""
    return string[1:].isdigit() or string.isdigit()


if __name__ == '__main__':

    n = ''
    while not is_str_int(n) and n != 'exit':
        n = input('input an integer: ')

    if n == 'exit':
        print('ok, bye!')
        exit()

    res = to_literals(n)
    print(f'you input: {n}, so {res}')
