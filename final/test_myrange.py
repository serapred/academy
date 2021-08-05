import unittest
import random

from random import randint, random
from itertools import zip_longest


from myrange import new_range


class TestMyRangeFunction(unittest.TestCase):

    def test_empty(self):
        # just to use it, and fail to something
        # could not think of anything better...
        self.assertTrue(list(new_range(-1)) == list(new_range(0)) == [])

    def test_len(self):
        l1, r1 = range(-2, -4, -3), new_range(-2, -4, -3)
        l2, r2 = range(-2, -4, 3), new_range(-2, -4, 3)
        l3, r3 = range(-2, 4, -3), new_range(-2, 4, -3)
        l4, r4 = range(-2, 4, 3), new_range(-2, 4, 3)
        l5, r5 = range(2, -4, -3), new_range(2, -4, -3)
        l6, r6 = range(2, -4, 3), new_range(2, -4, 3)
        l7, r7 = range(2, 4, -3), new_range(2, 4, -3)
        l8, r8 = range(2, 4, 3), new_range(2, 4, 3)
        l9, r9 = range(2, 4), new_range(2, 4)
        l10, r10 = range(2), new_range(2)
        l11, r11 = range(-2), new_range(-2)

        a = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11]
        b = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11]
        la, lb = ([len(r) for r in a], [len(r) for r in b])
        self.assertEqual(la, lb)

    def test_values(self):
        # s: start, i: increment, e: end, p: params
        for q in range(0, 10000):
            s, i = randint(0, 100), randint(1, 100)
            i *= -1 if random() > 0.5 else 1

            e, p = s + (i * randint(1, 100)), randint(1, 3)
            args = [s, e, i][:p]
            for i, j in zip_longest(
                    new_range(*args),
                    range(*args),
                    fillvalue=object):
                self.assertTrue(i == j)

    def test_slices(self):
        pass  # todo: compare slicing

    def test_errors(self):
        pass  # compare error generation


if __name__ == '__main__':
    unittest.main()
