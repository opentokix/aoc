#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_lists(f):w
    """
    This function takes a file with two colums of numbers and returns two lists of numbers.
    called one and two.
    """
    one = []
    two = []
    for line in f:
        x, y = line.split()
        one.append(int(x))
        two.append(int(y))
    return one, two

def main():
    f = open("input", "r")
    one, two = make_lists(f)
    one.sort()
    two.sort()
    result = 0
    for i in range(len(one)):
        result += abs(one[i] - two[i])
    print(result)
    f.close()


if __name__ == '__main__':
    main()
