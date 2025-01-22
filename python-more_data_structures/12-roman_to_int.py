#!/usr/bin/python3

def roman_to_int(roman_string):
    d = {"X":10, "I":1, "V":5, "L":50, "C":100}
    c = roman_string
    sum = d[c[0]]
    for i in range(1, len(c)):
        if d[c[i]] <= d[c[i-1]]:
            sum += d[c[i]]
        else:
            sum += d[c[i]] - 2 * d[c[i-1]]
    return sum
