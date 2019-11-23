def insertionSort1(n, arr):
    num = arr[-1]
    idx = n - 2
    while num < arr[idx] and idx >= 0:
        arr[idx+1] = arr[idx]
        print(' '.join(map(str, arr)))
        idx -= 1

    arr[idx+1] = num
    print(' '.join(map(str, arr)))


n = int(input())

arr = list(map(int, input().rstrip().split()))

insertionSort1(n, arr)
