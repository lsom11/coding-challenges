
def sort_by_k(arr, k):
    arr.sort(key=lambda x: x[k])
    for subarr in arr:
        print(' '.join(map(lambda x: str(x), subarr)))


n, m = map(int, input().split())


arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())

sort_by_k(arr, k)
