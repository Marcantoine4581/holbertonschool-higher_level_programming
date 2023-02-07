#!/usr/bin/python3
"""Defines the class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Funtion that validates value.
        
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError : If value is not an int.
            ValueError: if value <= 0.     
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
