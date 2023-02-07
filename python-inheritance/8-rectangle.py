#!/usr/bin/python3
"""Defines the class Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a resctangle."""

    def __init__(self, width, height):
        """
        Args:
            width (int): The wight og the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width) 
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
