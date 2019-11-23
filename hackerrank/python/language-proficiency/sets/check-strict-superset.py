s = set(input().split(' '))
T = int(input())
superset = True

for _ in range(T):
    other_set = set(input().split(' '))
    if len(other_set.intersection(s)) != len(other_set) or len(other_set.difference(s)) != 0:
        superset = False

print(superset)
