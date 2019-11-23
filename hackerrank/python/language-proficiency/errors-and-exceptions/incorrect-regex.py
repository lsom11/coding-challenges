import re

T = int(input())

for i in range(T):
    S = input()
    try:
        re.compile(S)
        print(True)
    except re.error:
        print(False)
