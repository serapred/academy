"""
Write a program to convert hexadecimals into rgb and viceversa.
"""


def from_rgb(r, g, b, prefix='#'):
    return f'{prefix}{r:02X}{g:02X}{b:02X}'


def to_rgb(hexa, prefix='#'):
    return tuple(int(hexa[i:i + 2], 16) for i in (1, 3, 5))


if __name__ == '__main__':
    a = from_rgb(0, 200, 200)
    b = to_rgb(a)
    print(a, b)
