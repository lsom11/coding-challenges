from collections import Counter

X = int(input())
sizes = Counter([int(x) for x in input().split()])
N = int(input())
total = 0

for i in range(N):
    size, price = map(int, input().split())

    if sizes[size]:
        sizes[size] -= 1
        total += price

print(total)
