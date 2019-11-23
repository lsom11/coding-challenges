#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    d = dict()
    contains = 'NO'

    for char in s1:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for char in s2:
        if char in d:
            contains = 'YES'
            break

    return contains


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
