import os

def diagonalDifference(arr):
    diff = 0
    for i in range(len(arr)):
        diff += arr[i][i]
        diff -= arr[i][len(arr) - i - 1]

    return abs(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
