#!/usr/bin/python3

"""
This module contains the function text_indentation
"""


def text_indentation(text):

    """
    function prints a text with 2 new lines after each of these characters:
    (., ?)
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        raise ValueError("text must not be empty")
    special_chars = [".", ":", "?"]
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
