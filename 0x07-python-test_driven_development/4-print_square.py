#!/usr/bin/python3
"""print a square with the character #."""


def print_square(size):
    """prints a square with the character #."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
