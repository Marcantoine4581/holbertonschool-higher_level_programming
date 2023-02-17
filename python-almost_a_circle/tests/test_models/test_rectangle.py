#!/usr/bin/python3
"""Unittest for class Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from contextlib import redirect_stdout
import os


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

    def test_type_error_init(self):
        self.assertRaisesRegex(
            TypeError, "width must be an integer", Rectangle, "1", 2)
        self.assertRaisesRegex(
            TypeError, "height must be an integer", Rectangle, 1, "2")
        self.assertRaisesRegex(
            TypeError, "x must be an integer", Rectangle, 1, 2, "3")
        self.assertRaisesRegex(
            TypeError, "y must be an integer", Rectangle, 1, 2, 3, "4")

    def test_width_or_heigth_equal_zero(self):
        self.assertRaisesRegex(
            ValueError, "width must be > 0", Rectangle, 0, 2)
        self.assertRaisesRegex(
            ValueError, "height must be > 0", Rectangle, 3, 0)

    def test_str_for_Rectangle(self):
        r1 = Rectangle(10, 10, 10, 10, 20)
        self.assertEqual(str(r1), "[Rectangle] (20) 10/10 - 10/10")

    def test_area(self):
        r = Rectangle(5, 4)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        r1 = Rectangle(4, 2)
        output = "####\n####\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r1.display()
            result = buffer.getvalue()
        self.assertEqual(result, output)

        r2 = Rectangle(4, 2, 1, 3, 50)
        output = "\n\n\n ####\n ####\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            r2.display()
            result = buffer.getvalue()
        self.assertEqual(result, output)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(45)
        self.assertEqual(r.id, 45)
        r.update(45, 20)
        self.assertEqual(r.width, 20)
        r.update(45, 20, 30, 10, 8)
        self.assertEqual(r.y, 8)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=2)
        self.assertEqual(r.height, 2)

        r.update(width=1, height=2, x=1, y=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        r = Rectangle(10, 15, 5, 3, 32)
        self.assertEqual(r.to_dictionary(), {'id': 32, 'width': 10, 'height': 15,
                                             'x': 5, 'y': 3})

    def test_create(self):
        r1 = Rectangle(3, 5, 1, 4)
        r2 = Rectangle.create(**{"x": 1, "y": 4, "id": 1, "height": 5, "width": 3})
        self.assertIsNot(r1, r2)

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            output = f.read()
        self.assertEqual('[{"x": 2, "y": 8, "id": 5, "height": 7, \
"width": 10}]', output)
        os.remove("Rectangle.json")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            output = f.read()
        self.assertEqual('[]', output)
        os.remove("Rectangle.json")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            output = f.read()
        self.assertEqual('[]', output)
        os.remove("Rectangle.json")

    def test_load_to_file(self):
        r = Rectangle(3, 5)
        Rectangle.save_to_file([r])
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].width, 3)
        self.assertEqual(rectangles[0].height, 5)
        os.remove("Rectangle.json")

        r = Rectangle.load_from_file()
        self.assertTrue(isinstance(r, list))
        self.assertEqual(r, [])

if __name__ == "__main__":
    unittest.main()
