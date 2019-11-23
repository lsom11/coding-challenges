
def loop(n: int):
    i = 1
    while i <= 10:
        print(str(n) + ' x ' + str(i) + ' = ' + str(n * i))
        i += 1


N = int(input())

loop(N)
