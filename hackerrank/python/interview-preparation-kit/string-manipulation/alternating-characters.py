#!/bin/python3

import os


def alternatingCharacters(s):
    first = s[0]
    if (all(x == first for x in s)):
        return len(s) - 1
    else:
        count = 0
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
