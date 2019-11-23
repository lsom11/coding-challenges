from itertools import combinations_with_replacement

S, k = input().split(' ')
k = int(k)
S = sorted(S)

combos = list(combinations_with_replacement(S, k))

for combo in combos:
    print(''.join(combo))


