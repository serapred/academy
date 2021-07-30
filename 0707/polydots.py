"""
Write a function that takes a positive integer num and calculates how many dots exist
in a pentagonal shape around the center dot on the Nth iteration.

In the image below you can see the first iteration is only a single dot. On the second,
there are 6 dots. On the third, there are 16 dots, and on the fourth there are 31 dots.
/files/polydots.png

Return the number of dots that exist in the whole pentagon on the Nth iteration.

Ex:
pentagonal(1) ➞ 1
pentagonal(2) ➞ 6
pentagonal(3) ➞ 16
pentagonal(8) ➞ 141

Bonus:
Try to generalize the problem for any polygonal shape (as in  number of vertex != 5)
"""


def polygon_dots(sides, i):
    return 1 + sides * (i * (i - 1)) // 2


if __name__ == '__main__':

    from sys import argv
    print(polygon_dots(int(argv[1]), int(argv[2])))
