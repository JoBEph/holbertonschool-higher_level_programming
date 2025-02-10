#!/usr/bin/python3
"""overite file and append file txt and return the number of characters"""


def append_write(filename="", text=""):

    with open(filename, "a", encoding="utf-8") as f:
        data_file = f.write(text)
        return (data_file)
