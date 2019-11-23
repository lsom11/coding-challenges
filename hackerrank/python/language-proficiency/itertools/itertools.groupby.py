from itertools import groupby

S = input()

modified_string = [(len(list(c)), int(k)) for k, c in groupby(S)]

print(*modified_string)
