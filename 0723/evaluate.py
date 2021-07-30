"""
Basic Arithmetic Operations on a String Number

Create a function to perform basic arithmetic operations that includes addition, subtraction,
multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we
are going to have only two numbers between 1 valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

Ex:
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24
arithmetic_operation("12 - 12") ➞ 0 // 12 - 12 = 0
arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144
arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1
"""

from operator import mul, add, sub, truediv


def arithmetic_operation(op):
    # not allowed
    return eval(op)


def arithmetic_operation(op):
    # allows floating point ('/' instead of '//')
    funcs = {'+': add, '*': mul, '-': sub, '/': truediv}
    sign = ''
    for s in funcs:
        if s in op:
            func = funcs[s]
            sign = s
            break
    a, b = op.split(sign)

    if sign == '/' and b == 0:
        return -1

    return func(float(a), float(b))


if __name__ == '__main__':
    from sys import argv
    op = argv[1]
    res = arithmetic_operation(op)
    print(f'{op} = {res}')
