"""
Function that adds two integers
"""

def add_integer(a, b=98):
    """
    Function that adds two integers

    >>> add_integer(1, 2)
    3
    >>> add_integer(2, 3)
    5
    >>> add_integer(3, 4)
    7
    >>> add_integer(4, 'a')
    Traceback (most recent call last):
            ...
    TypeError: b must be an integer

    >>> add_integer('b', 6)
    Traceback (most recent call last):
            ...
    TypeError: a must be an integer
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