#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not insistance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not insistance(b, float))):
        raise TypeError("b must be an integer")
    Return (int(a) + int(b))
