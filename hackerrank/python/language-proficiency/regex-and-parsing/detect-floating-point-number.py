import re

N = int(input())

for _ in range(N):
    M = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', M)))
