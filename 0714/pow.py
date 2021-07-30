"""
define two functions (one iterative, one with list comprehension)
to return a list of the squares of the numbers from 1 to 10.
"""


def mypow(nums, exp=2):
    ans = []
    for x in nums:
        ans.append(pow(x, exp))
    return ans


def mypow(nums, exp=2):
    return [pow(x, exp) for x in nums]


def mypow(nums, exp=2):
    yield from map(lambda x: pow(x, exp), nums)


if __name__ == '__main__':

    nums = range(10)

    print(list(mypow(nums)))
