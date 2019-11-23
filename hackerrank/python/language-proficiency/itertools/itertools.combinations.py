from itertools import combinations

S, k = input().split()

for i in range(1, int(k) + 1):
    for e in combinations(sorted(S), i):
        print(''.join(e))
