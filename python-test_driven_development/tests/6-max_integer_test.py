#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_mixed(self):
        self.assertEqual(max_integer([1, -2, 3, 0]), 3)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_none(self):
        self.assertIsNone(max_integer())

if __name__ == '__main__':
    unittest.main()
