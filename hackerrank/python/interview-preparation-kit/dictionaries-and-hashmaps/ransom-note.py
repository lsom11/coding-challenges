from collections import Counter

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    d = Counter(note)
    for word in magazine:
        if word in d:
            d[word] -= 1
    if all(x <= 0 for x in d.values()):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
