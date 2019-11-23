def average(array):
    removed_duplicates = set(array)
    return sum(removed_duplicates) / len(removed_duplicates)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
