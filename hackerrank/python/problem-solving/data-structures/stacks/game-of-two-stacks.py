
import os
import sys


def twoStacks(x, a, b):
    count = 0
    current_sum = 0
    while current_sum < x:
        if a[0] <= b[0] and len(a):
            temp = a.pop(0)

            if temp + current_sum > x:
                break
            current_sum += temp
            count += 1
        elif len(b):
            temp = b.pop(0)
            if temp + current_sum > x:
                break
            current_sum += temp
            count += 1
        else:
            break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
