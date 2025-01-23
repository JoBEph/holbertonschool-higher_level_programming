#!/usr/bin/python3

def raise_exception():
    i = -1
    if i < 0:
        raise ValueError("Sorry, no numbers below zero")
    return i
