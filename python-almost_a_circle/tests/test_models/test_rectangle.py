#!/usr/bin/python3
"""Unittest for class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test the instantiation of the class Rectangle"""

    def test_five_args(self):
        """Test instance attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)

    def test_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

if __name__ == "__main__":
    unittest.main()
