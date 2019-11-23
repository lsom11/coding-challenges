from math import sqrt
from itertools import count, islice

T = int(input())


def check_if_prime(n):
    if n < 2:
        print('Not prime')
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            print('Not prime')
            return False

    print('Prime')
    return True


for i in range(T):
    n = int(input())
    check_if_prime(n)
