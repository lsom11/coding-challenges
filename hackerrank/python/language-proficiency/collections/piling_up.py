from collections import deque
N = int(input())

for _ in range(N):
    stackable = True
    input()
    d = deque(map(int, input().strip().split()))
    if (d[0] >= d[-1]):
        max = d.popleft()
    else:
        max = d.pop()
    while d:
        if (len(d) == 1):
            if (d[0] <= max):
                break
            else:
                stackable = False
                break
        else:
            if d[0] <= max and d[-1] <= max:
                if d[0] >= d[-1]:
                    max = d.popleft()
                else:
                   max = d.pop()
            elif d[0] <= max:
                max = d.popleft()
            elif d[-1] <= max:
                max = d.pop()
            else:
                stackable = False
                break

    if stackable:
        print("Yes")
    else:
        print("No")
