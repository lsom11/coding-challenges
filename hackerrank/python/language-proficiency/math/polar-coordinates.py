from cmath import phase

z = complex(input())

r = abs(z)
angle = phase(z)

print(r)
print(angle)
