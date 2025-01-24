#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
        
    special_chars = [".", ":", "?", "!"]
    i = 0
    while i < len(text):
        if text[i] in special_chars:
            print(text[i], end="")
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
