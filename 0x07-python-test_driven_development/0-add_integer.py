#!/usr/bin/python3
"""
Function that adds two integers
"""

def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    types = [float, int]


    if not type(a) in types:
        raise TypeError("a must be an integer")

    if not type(b) in types:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()