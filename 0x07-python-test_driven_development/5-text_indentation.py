#!/usr/bin/python3
"""Print the indentation of a string."""


def text_indentation(text):
    """Print the indentation of a string."""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    last = 0

    for i in range(len(text)):
        if text[i] in ('.', '?', ':'):
            print(text[last:i + 1].strip(), end='\n\n')
            last = i + 1

