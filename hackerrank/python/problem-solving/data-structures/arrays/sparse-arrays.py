#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.


def matchingStrings(strings, queries):
    d = dict()
    output = []
    for s in strings:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    for q in queries:
        if q in d:
            output.append(d[q])
        else:
            output.append(0)
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
