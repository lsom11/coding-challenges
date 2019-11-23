N = int(input())
dict = {}

for i in range(N):
    string = input()
    if string in dict:
        dict[string] += 1
    else:
        dict[string] = 1

print(len(dict))
for key in dict:
    print(dict[key], end=" ")
