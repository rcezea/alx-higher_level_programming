#!/usr/bin/python3

def add_integer(a, b=98):
    valuetype = (int, float)
    if not isinstance(a, valuetype):
        raise TypeError("a must be an integer")
    if not isinstance(b, valuetype):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a+b
