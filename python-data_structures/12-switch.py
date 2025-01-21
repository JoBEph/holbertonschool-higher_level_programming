#!/usr/bin/python3

def switch(my_list=[]):
    if len(my_list) > 1:
        my_list[0], my_list[1] = my_list[1], my_list[0]
    return my_list
