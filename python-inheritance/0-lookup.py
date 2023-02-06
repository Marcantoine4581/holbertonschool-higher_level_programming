#!/usr/bin/python3
"""function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """
    Arg:
        obj : the oject.
    Return:
        the list of available attributes and methods of an object.
    """
    return dir(obj)
