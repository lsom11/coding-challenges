
T = int(input())

for _ in range(T):
    N, K = map(lambda x: int(x), input().split())

    maximum = 0

    for j in range(1, N):
        for k in range(j + 1, N + 1):
            h = j & k
            if K > h > maximum:
                maximum = h

    print(maximum)
