#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    result = 0
    for arg in argv:
        result += int(arg)
    print(result)
    