S = input()

lower = []
upper = []
odds = []
evens = []

for char in S:
    if char.isdigit():
        if int(char) % 2 == 0:
            evens.append(char)
        else:
            odds.append(char)
    else:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)

lower.sort()
upper.sort()
odds.sort()
evens.sort()

print(''.join(lower + upper + odds + evens))
