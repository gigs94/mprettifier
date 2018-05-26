import unittest
from mpretty import mpretty

class test_derived_use_cases(unittest.TestCase):

    def test_trillion(self):
        self.assertEqual(str(mpretty('9900000000000')), '9.9T')

    def test_more_than_trillion(self):
        self.assertEqual(str(mpretty('99999990000000000')), '99999.9T')

    def test_small(self):
        self.assertEqual(str(mpretty('234.25948')), '234.2')

if __name__ == '__main__':
    unittest.main()

