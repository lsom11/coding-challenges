from collections import Counter


def one_away(a, b):
    if abs(len(a) - len(b)) > 1:
        print(False)
    count = 0

    c = Counter(a)
    for char in b:
        if char in c:
            c[char] -= 1
    count += sum(c.values())
    if count > 1:
        return False
    else:
        return True


print(one_away('pale', 'ple'))  # True
print(one_away('pales', 'pale'))  # True
print(one_away('pale', 'bake'))  # False
