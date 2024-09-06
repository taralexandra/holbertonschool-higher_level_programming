#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    num = 0

    for arg in argv[1:]:
        num += int(arg)

    print(num)
