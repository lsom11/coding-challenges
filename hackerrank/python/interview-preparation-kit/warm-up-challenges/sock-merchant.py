n = int(input())
sock_arr = list(map(lambda x: int(x), input().split()))
d = dict()
count = 0

for i in range(len(sock_arr)):
    sock = sock_arr[i]
    if sock in d:
        d[sock] += 1
    else:
        d[sock] = 1

for key in d:
    count += d[key] // 2

print(count)
