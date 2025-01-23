#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    result = 0
    try:
            while result < x:
                print("{}".format(my_list[result]), end="")
                result += 1
    except IndexError:
            pass
    print()
    return result
