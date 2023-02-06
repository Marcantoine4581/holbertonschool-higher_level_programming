#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """
    Args:
        obj : the oject
        a_class: the specified class
    Return:
        True if the object is exactly an instance 3 of the specified class.
        otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
