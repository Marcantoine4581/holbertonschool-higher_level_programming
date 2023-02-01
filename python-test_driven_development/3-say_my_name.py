#!/usr/bin/python3
"""function that prints "My name is <first name> <last name>" """


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): first parameter
        last_name (str): second parameter

    Raises:
        TypeError:
            if elements are not strings
    Return: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
