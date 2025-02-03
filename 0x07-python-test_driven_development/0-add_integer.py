#!/usr/bin/python3
"""Add two integers together."""


def add_integer(a, b=98):
    """Add two integers together."""
    if a is None:
        raise TypeError(
            "add_integer() missing 1 required positional argument: 'a'")
    types = [float, int]
    if not type(a) in types:
        raise TypeError("a must be an integer")
    if not type(b) in types:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
