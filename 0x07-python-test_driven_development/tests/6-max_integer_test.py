#!/usr/bin/python3
"""
Test module to find the max integer in a list.
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function
    """

    def test_max_integer(self):
        """Check max integer."""
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)
        result = max_integer([12, 9, 7, 2])
        self.assertEqual(result, 12)

    def test_isint(self):
        """Check variable against an integer."""
        var = 1
        self.assertTrue(max_integer([var, 2]) == 2)
        x = 5
        self.assertTrue(max_integer([1, x]) == x)

    def test_same_entry(self):
        """Check max integer if the same."""
        a = 50
        self.assertEqual(max_integer([a, a, a, a]), a)

    def test_float_integer(self):
        """Check if float is the max integer."""
        self.assertEqual(max_integer([4.0, 3, 2]), 4.0)

    def test_one_entry(self):
        """Check only one entry."""
        self.assertEqual(max_integer([10]), 10)

    def test_negative_integer(self):
        """Only negative integers."""
        self.assertEqual(max_integer([-1, -2, -5]), -1)

    def test_no_argument(self):
        """No argument provided."""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Empty list provided."""
        self.assertEqual(max_integer([]), None)

    if __name__ == "__main__":
        unittest.main()
