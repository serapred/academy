import unittest
from psplit import psplit


class TestPsplitFunction(unittest.TestCase):

    def test_empty(self):
        # just to use it, and fail to something
        # could not think of anything better...
        self.assertTrue(list(psplit('')) == ())

    def test_domain(self):
        self.assertEqual(set('((()))()()'), set('()'))

    def test_single(self):
        self.assertEqual(list(psplit('()')), ['()'])

    def test_nested(self):
        self.assertEqual(list(psplit('((()))')), ['((()))'])

    def test_score_gt_zero(self):
        with self.assertRaises(ValueError):
            list(psplit('((('))

    def test_score_lt_zero(self):
        with self.assertRaises(ValueError):
            list(psplit('())'))


if __name__ == '__main__':
    unittest.main()
