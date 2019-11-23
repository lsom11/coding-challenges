import itertools

N = int(input())
letters = input().split()
K = int(input())

num = 0
den = 0
for e in itertools.permutations(letters, K):
    den += 1
    num += 'a' in e[:K]
print(num*1.0/den)
