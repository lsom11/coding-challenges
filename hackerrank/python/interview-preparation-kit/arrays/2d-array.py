#!/bin/python3

import math
import os
import random
import re
import sys


def getSum(arr, i, j):
    sum = 0
    sum += arr[i - 1][j - 1]
    sum += arr[i - 1][j]
    sum += arr[i - 1][j + 1]
    sum += arr[i][j]
    sum += arr[i + 1][j - 1]
    sum += arr[i + 1][j]
    sum += arr[i + 1][j + 1]

    return sum

# Complete the hourglassSum function below.


def hourglassSum(arr):
    max_sum = -63

    for i in range(1, 5):
        for j in range(1, 5):
            sum = getSum(arr, i, j)
            if sum > max_sum:
                max_sum = sum

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
