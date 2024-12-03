#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_lists(f):
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

def count_occurances(number, source):
    """
    This function takes a number and a list and returns the number of times the number appears in the list.
    """
    count = 0
    for i in range(len(source)):
        if source[i] == number:
            count += 1
    return count

def main():
    f = open("input", "r")
    one, two = make_lists(f)
    one.sort()
    two.sort()
    count = 0
    for i in range(len(one)):
        x = count_occurances(one[i], two)
        count += x * one[i]
    f.close()
    print(count)

if __name__ == '__main__':
    main()
