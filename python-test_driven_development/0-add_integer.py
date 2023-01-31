#!/usr/bin/python3
""" function that adds 2 integers"""


def add_integer(a, b=98):
    """Returns an integer: the addition of a and b.

    TypeCast:
        float arguments are casted to intergers.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
