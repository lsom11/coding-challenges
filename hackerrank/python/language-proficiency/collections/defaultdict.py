from collections import defaultdict

d = defaultdict(list)

n, m = (int(i) for i in input().split())

for A in range(n):
    d[input()].append(A + 1)

for B in range(m):
    print(*d.get(input(), [-1]), sep=' ')
