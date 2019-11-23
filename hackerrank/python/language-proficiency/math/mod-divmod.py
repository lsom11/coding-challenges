a, b = int(input()), int(input())

l = [a//b, a % b]
print(l[0])
print(l[1])
print("({0}, {1})".format(l[0], l[1]))
