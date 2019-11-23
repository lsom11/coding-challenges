from itertools import combinations
from functools import reduce

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    min = None
    max = None
    subsets = list(combinations(arr, 4))
    for subset in subsets:
        sum = reduce(lambda a, b: a + b, subset)
        if not min or sum < min:
            min = sum
        if not max or sum > max:
            max = sum

    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
