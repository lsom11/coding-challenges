n, m = list(map(lambda x: int(x), input().split()))
arr = list(map(lambda x: int(x), input().split()))

total_happiness = 0

A = set(map(lambda x: int(x), input().split()))
B = set(map(lambda x: int(x), input().split()))

for num in arr:
    if num in A:
        total_happiness += 1
    if num in B:
        total_happiness -= 1

print(total_happiness)
