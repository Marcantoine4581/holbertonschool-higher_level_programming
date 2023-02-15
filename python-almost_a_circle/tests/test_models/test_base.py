#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test the instantiation of the class Base"""

    def test_init(self):
        """Test of Base() for assigning automatically an ID"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        """Test of Base() for assigning automatically an ID + 1 of the previous"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

        """Test of Base(89) saving the ID passed"""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

        b4 = Base()
        self.assertEqual(b4.id, 3)

if __name__ == "__main__":
    unittest.main()
