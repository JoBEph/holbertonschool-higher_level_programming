#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    c = list(roman_string)
    result = 0
    for i in range(len(c)):
        if i > 0 and d[c[i]] > d[c[i-1]]:
            result += d[c[i]] - 2 * d[c[i-1]]
        else:
            result += d[c[i]]
    return result
