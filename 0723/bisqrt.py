"""
Get Sqrt of a Number Using Bisection Search
Create a function that uses bisection search to compute the approximative value of the square root of a
number.

Use any integer or float as an argument.
Use a delta variable of 0.01 to know when a result is valid (i.e. if the result squared is between n - delta
and n + delta, it's considered valid).
Examples
bisec_sqrt(69) ➞ 8.307
bisec_sqrt(16) ➞ 4.0
bisec_sqrt(12984771) ➞ 3603.439
bisec_sqrt(12.21) ➞ 3.494
Notes
Round values up to 3 digits (round() method).
Please use bisection search: it may take more lines but the efficiency is incredible!
"""


def bisectroot(x, eps=0.1, precision=3, n=1000):

    low = 0
    high = x
    y = (high + low) / 2.0

    while abs(y**2 - x) >= eps and n > 0:
        if y**2 < x:
            low = y
        else:
            high = y

        y = (high + low) / 2.0
        n -= 1

    return round(y, precision)


if __name__ == '__main__':

    from sys import argv
    ans = bisectroot(float(argv[1]))
    print(f'a square root approximation: {ans}')
