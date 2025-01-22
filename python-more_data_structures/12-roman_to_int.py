#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    d = {"X": 10, "I": 1, "V": 5, "L": 50, "C": 100, "D": 500, "M": 1000}
    prev_value = 0
    result = 0
    for i in roman_string:
        value = d.get(i, 0)
        if prev_value < value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
        return result
