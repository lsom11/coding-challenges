from itertools import permutations

S, k = input().split()

for e in permutations(sorted(S), int(k)):
    print(''.join(e))
