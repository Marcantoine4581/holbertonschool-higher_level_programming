#!/usr/bin/python3
"""Unittest fos class Square"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from contextlib import redirect_stdout
import os


class TestSquare(unittest.TestCase):
    """Test the instantiation of the class Square"""

    def test_four_args(self):
        """Test instance attributes"""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 4)

    def test_one_args(self):
        s1 = Square(2)
        s2 = Square(5)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_type_error_init(self):
        self.assertRaisesRegex(
            TypeError, "width must be an integer", Square, "1", 2)
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Square, 1, "2")
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Square, 1, 2, "3")

    def test_size_equal_zero(self):
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Square, 0)

    def test_str_for_Square(self):
        s1 = Square(10, 5, 7, 20)
        self.assertEqual(str(s1), "[Square] (20) 5/7 - 10")

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s1 = Square(4)
        output = "####\n####\n####\n####\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            s1.display()
            result = buffer.getvalue()
        self.assertEqual(result, output)

        s2 = Square(4, 1, 3, 50)
        output = "\n\n\n ####\n ####\n ####\n ####\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            s2.display()
            result = buffer.getvalue()
        self.assertEqual(result, output)

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(45)
        self.assertEqual(s.id, 45)
        s.update(45, 20)
        self.assertEqual(s.size, 20)
        s.update(45, 20, 30, 8)
        self.assertEqual(s.y, 8)

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(size=2)
        self.assertEqual(s.size, 2)

        s.update(sizet=2, x=1, y=2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        s = Square(15, 5, 3, 32)
        self.assertEqual(s.to_dictionary(), {'id': 32, 'size': 15,
                                             'x': 5, 'y': 3})

    def test_create(self):
        s1 = Square(3, 5, 1)
        s2 = Square.create(**{'id': 2, 'size': 3, 'x': 5, 'y': 1})
        self.assertIsNot(s1, s2)

    def test_save_to_file(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4, 5, 8)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            output = f.read()
        self.assertEqual('[{"id": 8, "size": 10, "x": 7, "y": 2}, \
{"id": 8, "size": 2, "x": 4, "y": 5}]', output)
        os.remove("Square.json")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            output = f.read()
        self.assertEqual('[]', output)
        os.remove("Square.json")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            output = f.read()
        self.assertEqual('[]', output)
        os.remove("Square.json")

    def test_load_to_file(self):
        r = Square(3)
        Square.save_to_file([r])
        rectangles = Square.load_from_file()
        self.assertIsInstance(rectangles[0], Square)
        self.assertEqual(rectangles[0].size, 3)
        os.remove("Square.json")

        r = Square.load_from_file()
        self.assertTrue(isinstance(r, list))
        self.assertEqual(r, [])

if __name__ == "__main__":
    unittest.main()
