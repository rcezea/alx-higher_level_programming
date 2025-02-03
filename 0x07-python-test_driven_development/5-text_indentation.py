#!/usr/bin/python3
"""Print the indentation of a string."""


def text_indentation(text):
    """Print the indentation of a string."""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = ''

    for i in range(len(text)):
        if text[i - 1] in ('.', '?', ':'):
            new_text += '\n\n'
            if text[i] == ' ':
                continue
        new_text += text[i]
    print(new_text)
