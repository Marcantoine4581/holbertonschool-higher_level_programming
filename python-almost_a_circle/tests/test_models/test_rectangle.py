#!/usr/bin/python3
"""Unittest for class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test the instantiation of the class Rectangle"""

    def test_init(self):
        """Test instance attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

if __name__ == "__main__":
    unittest.main()
