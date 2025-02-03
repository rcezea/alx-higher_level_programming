#!/usr/bin/python3
"""Print the indentation of a string."""


def text_indentation(text):
    """Print the indentation of a string."""

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    last = 0

    new_text = ''

    for i in range(len(text)):
        if text[i] in ('.', '?', ':'):
            new_text += text[last:i + 1].strip() + '\n\n'
            last = i + 1
    new_text += text[last:].strip()

    print(new_text if new_text else text)
