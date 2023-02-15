#!/usr/bin/python3
"""Unittest for class Base"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test the instantiation of the class Base"""

    def test_init(self):
        """Test of Base() for assigning automatically an ID + 1 of the previous"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_None(self):
        """Test for is None"""
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, b3.id - 2)

    def test_unique_id(self):
        """Test of Base(89) saving the ID passed"""
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

if __name__ == "__main__":
    unittest.main()
