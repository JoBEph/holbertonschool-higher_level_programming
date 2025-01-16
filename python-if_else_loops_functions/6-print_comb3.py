#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        if x < 9 or y < 9:
            print("{:02d}, ".format(x * 10 + y), end='')
print("{:02d}".format(89))
