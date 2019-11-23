phoneBook = {}
N = int(input())
for i in range(0, N):
    person = input().split()
    phoneBook[person[0]] = person[1]

while True:
    try:
        query = input()
        if query == '':
            break
        elif query in phoneBook:
            print(query + '=' + phoneBook[query])
        else:
            print('Not found')
    except EOFError:
        break
