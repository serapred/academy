"""
Write a function that uses bisection to find if a number is present
in a sorted sequence
"""

from bisect import bisect_left


def search(h, n):
    # one liner with bisect_left
    return (lambda x: x if h[x] == n else -1)(bisect_left(h, n, 0, len(h) - 1))


def search(haystack, needle):

    left, right = 0, len(haystack) - 1
    while left <= right:
        mid = (left + right) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] < needle:
            left = mid + 1
        else:
            right = mid - 1
    return -1
