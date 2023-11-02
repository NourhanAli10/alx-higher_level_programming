#!/usr/bin/python3
"""class to Add two integers or floats and return their sum."""


def add_integer(a, b=98):
    """
    This function takes two numeric values, 'a' and 'b',
    and returns their sum as an integer.
    If 'a' or 'b' is a float, it will be converted to an integer
    before performing the addition.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return sum
