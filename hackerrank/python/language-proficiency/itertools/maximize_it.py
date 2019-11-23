import itertools

K, M = map(int, input().split())
a = [[int(e)**2 for e in input().split()][1:] for _ in range(K)]
print(max(sum(e) % M for e in itertools.product(*a)))
