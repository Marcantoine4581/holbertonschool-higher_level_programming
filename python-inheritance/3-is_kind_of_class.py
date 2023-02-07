#!/usr/bin/python3
"""function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj : the oject
        a_class: the specified class
    Return:
        True, if the object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class.
        otherwise False.
    """
    return isinstance(obj, a_class)
