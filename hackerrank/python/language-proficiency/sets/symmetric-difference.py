M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))

l1 = a.difference(b)
l2 = b.difference(a)
l3 = sorted(l1.union(l2))

for num in l3:
    print(num)
