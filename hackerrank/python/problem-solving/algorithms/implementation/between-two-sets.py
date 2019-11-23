#!/bin/python3

from functools import reduce
import os


def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    print(min_gcd, max_lcm)
    count = sum(
        [1 for x in range(max_lcm, min_gcd+1, max_lcm) if min_gcd % x == 0])

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
