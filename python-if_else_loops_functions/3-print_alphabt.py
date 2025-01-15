#!/usr/bin/python3
kicker = {'q', 'e'}
for alphabet in range(ord('a'), ord('z') + 1):
    if chr(alphabet) not in kicker:
         print(chr(alphabet), end="")
