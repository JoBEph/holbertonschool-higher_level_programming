#!/usr/bin/python3

def text_indentation(text):
    special_chars = [".", ":", "?", "!"]
    for idx, i in enumerate(text):
        if i in special_chars:
            print(i, end="\n")
            print()
        elif i == " ":
            if text[idx-1] in special_chars:
                continue
            else:
                print(i, end="")
        else:
            print(i, end="")
