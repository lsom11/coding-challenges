
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    for val in a[d:]:
        print(val, end=' ')

    for val in a[:d]:
        print(val, end=' ')
