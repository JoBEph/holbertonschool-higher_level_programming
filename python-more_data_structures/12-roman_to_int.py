#!/usr/bin/python3

def roman_to_int(roman_string):
    d = {"X": 10, "I": 1, "V": 5, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev_value = 0
    sum = 0
    for i in roman_string:
        value = d[i]
        if prev_value < value:
            sum += value - 2 * prev_value
        else:
            sum += value
        prev_value = value
        return sum
