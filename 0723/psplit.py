"""
Write a function that groups a string into parentheses cluster.
Each cluster should be balanced.

Examples
split("()()()") ➞ ["()", "()", "()"]
split("((()))") ➞ ["((()))"]
split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]
split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]

Notes:
All input strings will only contain parentheses.
Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.
"""


def p_to_n(char):
    if char not in '()':
        raise ValueError
    return -1 if char == ')' else 1


def psplit(parentheses):

    pmap = map(p_to_n, parentheses)
    start = finish = score = 0
    error = ValueError('the string is unbalanced')

    for i in pmap:
        score += i
        if score < 0:
            raise error
        if score == 0:
            yield parentheses[start:finish]

    if score != 0:
        raise error  # case (()


if __name__ == '__main__':
    from sys import argv
    print(' '.join(psplit(argv[1])))
