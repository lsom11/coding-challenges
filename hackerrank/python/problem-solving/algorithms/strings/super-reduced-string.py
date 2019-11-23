#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.


def superReducedString(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack) if len(stack) else 'Empty String'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    print(s)
    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
