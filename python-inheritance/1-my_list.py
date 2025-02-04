#!/usr/bin/python3

"""Mylist"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        Sorted_list = sorted(self)
        print(Sorted_list)
