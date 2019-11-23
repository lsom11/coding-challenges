#!/bin/python3

import os


def maximumToys(prices, k):
    prices.sort()

    total = 0
    for price in prices:
        if (k-price) > 0:
            total += 1
            k = k - price
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
