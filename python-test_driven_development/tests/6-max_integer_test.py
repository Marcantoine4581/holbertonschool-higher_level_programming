#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        """Test an unordered list of integers."""
        self.assertEqual(max_integer([2, 1, 4, 3]), 4)

        """Test a list with a beginning max value."""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

        """Test a list with a single element."""
        self.assertEqual(max_integer([4]), 4)

        """Test for only negative numbers in the list."""
        self.assertEqual(max_integer([-4, -2, -3, -1]), -1)
