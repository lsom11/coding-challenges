#!/bin/python3
from collections import Counter
import os

# Complete the isValid function below.


def isValid(s):
    c = Counter(s)
    l = list(c.values())
    l.sort(reverse=True)
    if all(x == 1 for x in l):
        return 'YES'
    else:
        val = l[1]
        first = l.pop(0)
        if all(x == val for x in l) and first - val == 1:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
