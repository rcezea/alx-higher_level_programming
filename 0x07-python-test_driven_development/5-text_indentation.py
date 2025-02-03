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
            new_text += '\n'
            arr.append(new_text.lstrip())
            new_text = ''
        new_text += text[i]
    arr.append(new_text.strip())

    size = len(arr)

    for i in range(size):
        if i == size - 1:
            print(arr[i], end='')
        else:
            print(arr[i])
