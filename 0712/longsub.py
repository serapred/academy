"""
Longest substring with no repeating characters

Write a function that returns the longest non-repeating substring for a string input.

Ex:
longest_nonrepeating_substring("abcabcbb") = "abc"
longest_nonrepeating_substring("abcdcdkqrt") = "abcdcdkqrt"
longest_nonrepeating_substring("aaaaaa")  = "a"
longest_nonrepeating_substring("abcde") = "abcde"
longest_nonrepeating_substring("abcda") = "abcd"

Notes:
If multiple substrings tie in length, return the one which occurs first.

Bonus: Can you solve this problem in linear time?
"""


from sys import argv


def lnrs(s):

    seen = {}         # look-up table
    i = j = 0         # i,j: sliding window
    off = ans = 0     # offset and answer
    length = len(s)

    # cicles until either j has exausted the string
    # or wouldn't be possible to outmach the current
    # answer
    while j < length and i + ans < length:
        # if the char was seen and its index
        # is inside the current window
        if s[j] in seen and seen[s[j]] > i:
            # slide i to the element on the
            # right of the seen one
            i = seen[s[j]]

        # if j is found, i = j + 1
        seen[s[j]] = j + 1
        j += 1

        # swap and update
        if j - i > ans:
            ans = j - i
            off = i

    return s[off:off + ans]


if __name__ == '__main__':

    print(lnrs(argv[1]))
