"""
Write a function that returns True if two arrays, when combined, form a consecutive sequence. A
consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive
sequence, but 1, 2, 4, 5 is not.

Examples
consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
consecutive_combo([44, 46], [45]) ➞ True
"""


def sequenced(l1, l2):
    # assumes repetition are not valid
    # for the definition of sequence
    l3 = sorted(l1 + l2)
    last = l3.pop(0)
    for i in l3:
        if i - last != 1:
            return False
        last = i
    return True


def sequenced(l1, l2):
    # better than sorting ? O(n)
    # assumes repetition are valid
    # for the definition of sequence
    start = min(min(l1), min(l2))
    finish = max(max(l1), max(l2))
    s1 = set(l1)
    s2 = set(l2)
    for i in range(start, finish):
        if i not in s1 and i not in s2:
            return False
    return True


if __name__ == '__main__':

    ins = [
        [[7, 4, 5, 1], [2, 3, 6]],
        [[1, 4, 6, 5], [2, 7, 8, 9]],
        [[1, 4, 5, 6], [2, 3, 7, 8, 10]],
        [[44, 46], [45]]
    ]

    for a, b in ins:
        ans = "not" if not sequenced(a, b) else ""
        print(f"{a} and {b} do {ans} form a sequence")
