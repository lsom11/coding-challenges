#!/bin/python3

import os


open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]
# Complete the isBalanced function below.


def isBalanced(s):
    stack = []
    # loop through the string
    for i in s:
        # if left side push to stack
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            # check if the corresponding bracket is already in the stack
            # pop from end if the last item corresponds to the end tag
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
