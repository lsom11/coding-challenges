#!/bin/python3

import os
from functools import reduce


def compare_stacks(s1, s2, s3):
    return s1 == s2 == s3


def do_sum(x1, x2): return x1 + x2


def equalStacks(h1, h2, h3):

    while True:
        s1 = reduce(do_sum, h1)
        s2 = reduce(do_sum, h2)
        s3 = reduce(do_sum, h3)
        if not h1 or not h2 or not h3:
            return 0
        if compare_stacks(s1, s2, s3):
            return s1
        if s1 >= s2 and s1 >= s3:
            h1.pop(0)
        elif s2 >= s3:
            h2.pop(0)
        else:
            h3.pop(0)
    return s1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
