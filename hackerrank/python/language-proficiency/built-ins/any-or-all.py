N = int(input())
M = list(map(lambda x: x, input().split()))


def check_palindromic(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev*10+dig
        n = n//10
    if(temp == rev):
        return True
    else:
        return False


if not all(int(num) > 0 for num in M):
    print(False)
else:
    if any(check_palindromic(int(x)) for x in M):
        print(True)
    else:
        print(False)
