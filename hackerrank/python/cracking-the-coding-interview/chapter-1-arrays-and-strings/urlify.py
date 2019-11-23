
def urlify(s):
    string = [x for x in s.split(' ')]
    if (len(string) == 1):
        print(''.join(string))
    else:
        for block in string:
            print(block, end='%20')


urlify('Mr John Smith')
urlify('testnospaces')
