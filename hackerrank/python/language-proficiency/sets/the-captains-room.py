from collections import Counter

K = int(input())
c = Counter(map(int, input().split(' ')))

for value in c:
    if c[value] == 1:
        print(value)
