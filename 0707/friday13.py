"""
Friday 13th

Given the month and year as numbers, return whether that month contains a Friday
13th.

Ex:
friday13(3, 2020) ➞ True
friday13(10, 2017) ➞ True
friday13(1, 1985) ➞ False

Bonus:
avoid using datetime functions

Hint:
if using modules, remember leaps
"""
from datetime import datetime


def friday13(year, month):
    return datetime(year, month, 13).weekday() == 4


if __name__ == '__main__':
    from sys import argv
    ans = 'not' if not friday13(argv[1], argv[2]) else ''
    print(f'month: {argv[1]} year: {argv[2]}', sep=' ')
    print(f'it does {ans} contain a friday 13')
