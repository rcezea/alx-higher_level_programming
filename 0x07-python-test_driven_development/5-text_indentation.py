#!/usr/bin/python3
"""Print the indentation of a string."""


def text_indentation(text):
    """Print the indentation of a string."""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = ''
    arr = []

    for i in range(len(text)):
        if text[i - 1] in ('.', '?', ':'):
            new_text += '\n\n'
            arr.append(new_text.lstrip())
            new_text = ''
        new_text += text[i]
    arr.append(new_text.strip())
