"""
Write a function that takes a list in input and
returns its flattened version.

EX:
1) IN [ ] OUT [ ]
2) IN [ 1, 2, (3, 4), 5 [6, 7]] OUT [1, 2, 3, 4, 5, 6, 7, 3]
3) IN [1, [2, 3, (4, 5), ('sei', 7, [8, 9]), 'dieci']] OUT [1, 2, 3, 4, 5, 'sei, 7, 8, 9, 'dieci']
"""

from itertools import chain


def shallow_flatten(shallow):
    return chain(*shallow)  # version one


def shallow_flatten(shallow):
    return sum(shallow, [])  # version two


def deep_flatten(deep):

    while deep:
        item = deep.pop()
        if isinstance(item, (tuple, list)):
            deep.extend(item)
        else:
            yield item


if __name__ == '__main__':

    a = [[1, 2, 3], 4, [5, 6, 7]]
    print(list(deep_flatten(a)))
