"""
Write a function insert_dash(num) /
that will insert dashes ('-') between each two odd numbers in num.
For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd number.
Note that the number will always be non-negative (>= 0).
"""


def insert_dash(num):
    res = ''
    head, num = num[0], num[1:]
    for c in num:
        res += head + '-' if int(head) % 2 and int(c) % 2 else head
        head = c
    res += c
    return res


if __name__ == '__main__':
    from sys import argv
    print(insert_dash(argv[1]))
