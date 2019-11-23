n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for _ in range(commands):
    command = input()
    try:
        if command == 'pop':
            s.pop()
        else:
            com, index = command.split(' ')
            index = int(index)
            if com == 'discard':
                s.discard(index)
            else:
                s.remove(index)
    except KeyError:
        pass


print(sum(s))
