
"""
German mathematician Christian Goldbach (1690-1764) conjectured that every even number greater than 2 can be represented by the sum of two prime numbers. For example, 10 can be represented as 3+7 or 5+5.
Your job is to make the function return a list containing all unique possible representations of n in an increasing order if n is an even integer; if n is odd, return an empty list. Hence, the first addend must always be less than or equal to the second to avoid duplicates.
Constraints: 2 < n < 32000 and n is even
Examples
26 --> ['3+23', '7+19', '13+13']
100 --> ['3+97', '11+89', '17+83', '29+71', '41+59', '47+53']
7--> []
"""


def primality(n):
    # naive

    # base case
    if n <= 3:
        return n > 1

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primality(n):
    # sqrt optimization

    if n <= 3:
        return n > 1

    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def primality(n):
    # while optimization

    # base case
    if n <= 3:
        return n > 1

    i = 2

    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def primality(n):
    # 6k +/- 1 optimization

    # base case
    if n <= 3:
        return n > 1

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5  # (1-4 excluded)

    # i**2 to cicle up until sqrt(n)
    while i**2 <= n:
        # 6k - 1 or 6k + 1
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes(n):
    for i in range(2, n):
        if primality(i):
            yield i


def goldbach(n):
    p, seen = set(primes(n)), set()
    for i in p:
        anti = n - i
        if anti in p and anti not in seen:
            seen.add(anti)
            yield i, anti


if __name__ == '__main__':

    num = int(input('insert even number: ')) or 0
    if num % 2:
        print('Goodbye.'), exit()
    print([f'{x}+{y}' for x, y in goldbach(num)])
