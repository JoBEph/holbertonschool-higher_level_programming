#!/usr/bin/env python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    total = sum([int(args) for args in args])
    print(total)
