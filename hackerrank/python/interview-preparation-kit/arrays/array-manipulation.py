#!/bin/python3

import os

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    max = 0
    total = 0
    l = [0 for i in range(n + 1)]
    for query in queries:
        a, b, k = query
        l[a - 1] += k
        l[b] -= k
    for i in l:
        total += i
        if total > max:
            max = total
    return max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
