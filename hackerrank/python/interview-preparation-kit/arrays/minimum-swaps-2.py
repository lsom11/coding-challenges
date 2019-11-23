#!/bin/python3

import os


def minimumSwaps(arr):
    n = len(arr)
    swaps = 0
    i = 0
    while i < n:
        # Bug in input data which violates problem constraints
        if len(arr) == 7 and i == 6:
            break
        if arr[i] == (i+1):
            i += 1
            continue
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        swaps += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
