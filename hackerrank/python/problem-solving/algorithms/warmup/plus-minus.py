#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zeros_count = 0

    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zeros_count += 1

    print(positive_count / len(arr))
    print(negative_count / len(arr))
    print(zeros_count / len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
