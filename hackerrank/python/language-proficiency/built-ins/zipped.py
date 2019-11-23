N, X = input().split(' ')
X = int(X)

b = [map(float, input().split()) for i in range(X)]

for i in zip(*b):
    print(sum(i) / X)
