from odd_iterator import OddIterator
import unittest


class OddIteratorTests(unittest.TestCase):

    def test_odd_iterator(self):
        it = OddIterator([1, 2, 3, 4, 5, 6, 7, 8])
        result = [i for i in it]
        self.assertEqual(result, [1, 3, 5, 7])
