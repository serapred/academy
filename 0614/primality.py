"""
Write a function That establishes an integer primality

Ex:
primality(4) ➞ False
primality(23) ➞ True
primality(5) ➞ True
primality(1) ➞ False
primality(47) -> True
primality(2) ➞ True
primality(100) ➞ False
"""


def primality(n):

    if n <= 3:
        return n > 1

    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':

    from sys import argv

    try:
        n = int(argv[1])
    except ValueError:
        print('not a valid integer. Bye.')
    else:
        ans = 'not' if not primality(n) else ''
        print(f'the number {n} is {ans} prime.')
