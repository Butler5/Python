from last_iterator import LastIterator
import unittest


class LastIteratorTest:
    def last_test(self):
        it = ([1,2,3,4,5,6,7,8], 3)
        result = [i for i in it]
        self.assertEqual(result, [6, 7, 8])

