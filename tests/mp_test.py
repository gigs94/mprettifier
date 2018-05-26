import unittest
import mprettifier

class test_mprettifier_use_cases(unittest.TestCase):

    def test_even_million(self):
        self.assertEqual(mprettifier('1000000'), '1M')

    def test_non_even_million(self):
        self.assertEqual(mprettifier('2500000.34'), '2.5M')

    def test_up_to_1k(self):
        self.assertEqual(mprettifier('532'), '532')

    def test_up_to_1k(self):
        self.assertEqual(mprettifier('1123456789'), '1.1B')

if __name__ == '__main__':
    unittest.main()

