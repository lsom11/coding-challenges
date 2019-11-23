#!/bin/python3

import os


# Complete the freqQuery function below.
def freqQuery(queries):
    d = dict()
    for query in queries:
        if query[0] == 1:
            if query[1] in d:
                d[query[1]] += 1
            else:
                d[query[1]] = 1
        elif query[0] == 2:
            if query[1] in d:
                d[query[1]] -= 1
        else:
            print('1' if query[1] in set(d.values()) else '0')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    freqQuery(queries)
