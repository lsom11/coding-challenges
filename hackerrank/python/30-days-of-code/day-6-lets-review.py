cases = int(input())

for word in range(cases):
    N = input()
    odds = []
    evens = []
    for i in range(0, len(N)):
        if i % 2 != 0:
            odds.append(N[i])
        else:
            evens.append(N[i])

    print(''.join(evens), ''.join(odds), )
