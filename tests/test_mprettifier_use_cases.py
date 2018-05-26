import unittest
from mpretty import mpretty

class test_mprettifier_use_cases(unittest.TestCase):

    def test_even_million(self):
        self.assertEqual(str(mpretty('1000000')), '1M')

    def test_non_even_million(self):
        self.assertEqual(str(mpretty('2500000.34')), '2.5M')

    def test_up_to_1k(self):
        self.assertEqual(str(mpretty('532')), '532')

    def test_billion(self):
        self.assertEqual(str(mpretty('1123456789')), '1.1B')

if __name__ == '__main__':
    unittest.main()

